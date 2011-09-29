# Copyright (C) 2011 by Blade Polska s.c.
# Full rights belong to Tomasz Kopczuk and Marcin Mincer.
# www.bladepolska.com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import datetime
import time

from django.db import connections

from . import MeasureIt
from .db import AskThePonyCursorWrapper

def get_connections_times():
    db_queries_time, db_time = 0., 0.
    for c in getattr(connections, '_connections'):
        if isinstance(connections._connections[c].cursor, AskThePony_return_cursor_wrapper):
            db_single_times = connections._connections[c].cursor.get_db_time()
            db_queries_time += db_single_times[0]
            db_time += db_single_times[1]

            return (db_queries_time, db_time)

class AskThePony_return_cursor_wrapper(object):
    def __init__(self, old_method, connection_wrapper):
        self.old_method = old_method
        self.connection_wrapper = connection_wrapper
        self.cursor = None

        self.time_spent_in_db = 0.
        self.time_spent_in_db_routines = 0.

    def __call__(self):
        start = datetime.datetime.now()
        try:
            self.cursor = AskThePonyCursorWrapper(self.old_method(), self)
            return self.cursor
        finally:
            stop = datetime.datetime.now()
            duration = stop - start
            self.time_spent_in_db_routines += (duration.microseconds + (duration.seconds + duration.days * 24. * 3600.) * 10.**6) / 10.**6
           # print "Master", duration, self.time_spent_in_db_routines

    def get_db_time(self):
        return self.time_spent_in_db, self.time_spent_in_db_routines

    def clear(self):
        self.time_spent_in_db = 0.
        self.time_spent_in_db_routines = 0.
        
class AskThePonyClientMiddleware(object):
    def process_request(self, request):
        if not hasattr(request, '_bp_phase'):
            request._bp_phase = 0
            request.time_of_request = [datetime.datetime.utcnow()]
            request.times=[time.time()]
            for c in getattr(connections, '_connections'):
                if not isinstance(connections._connections[c].cursor, AskThePony_return_cursor_wrapper):
                    print "Piggybacking cursor method"
                    old_method = connections._connections[c].cursor
                    setattr(connections._connections[c], 'cursor', AskThePony_return_cursor_wrapper(old_method, connections._connections[c]))
                else:
                    connections._connections[c].cursor.clear()
        else:
            request._bp_phase = 1
            if hasattr(request, 'times'):
                request.times.append(time.time())
                print get_connections_times(), "in entry middleware"
        return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        print "View:", view_func.__module__, view_func.__name__
        if not hasattr(request, '_view_func'):
            request._view_func = (view_func.__module__, view_func.__name__)
        return None

    def process_response(self, request, response):
        if hasattr(request, 'times') and hasattr(request, '_view_func'):
            if not hasattr(response, '_bp_phase'):
                response._bp_phase = 0
                request.times.append(time.time())
            elif len(request.times) == 3:
                path = request.path
                db_queries_time, db_time = get_connections_times()

                request_middleware_time = request.times[1] - request.times[0]
                total_view_time = request.times[2] - request.times[1]
                view_time = request.times[2] - request.times[1] - db_queries_time - db_time
                response_middleware_time = time.time() - request.times[2]
                s = getattr(response, 'status_code', 0)
                r = str(s)
                if s in (300, 301, 302, 307):
                    r += ' => %s' % response.get('Location', '?')

        #        print "%s, %.2fms, %.2fms (%.2fms in view alone, %.2fms in SQL queries, %.2fms in DB routines), %.2fms"  %(path, request_middleware_time*1000., total_view_time*1000., view_time*1000., db_queries_time*1000., db_time*1000., response_middleware_time*1000.)

                MeasureIt.addPageHit(time.time(), path, request._view_func, request.GET, r, request_middleware_time, view_time, response_middleware_time, db_queries_time, db_time)

        return response
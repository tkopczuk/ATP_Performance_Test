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

import jsonlib
import zlib

from django.conf import settings
from Queue import Queue
import socket
import thread
import time

MAX_FRAME = 20
UDP_IP=getattr(settings, 'ATP_UDP_IP', None)
UDP_PORT=getattr(settings, 'ATP_UDP_PORT', 80)
API_KEY=getattr(settings, 'ATP_API_KEY', '0')

class MeasureIt(object):
    lock = thread.allocate_lock()
    queue = Queue()
    to_be_sent = None

    def sendOutIfFull():
        if MeasureIt.queue.qsize() < 1 or not UDP_IP:
            return
        with MeasureIt.lock:
            if MeasureIt.to_be_sent is None:
                MeasureIt.to_be_sent = "[ "
            try:
                while True:
                    item = MeasureIt.queue.get_nowait()
                    item_json = jsonlib.write(item)
                    if len(MeasureIt.to_be_sent) + len(item_json) + 2 > MAX_FRAME and len(MeasureIt.to_be_sent) > 2:
                      #  print "Sending..."
                        MeasureIt.to_be_sent = "%s%s" %(MeasureIt.to_be_sent[:-1], ",\"%s\",%.2f ]" % (API_KEY, time.time()))
                        sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM ) 
                        sock.sendto( zlib.compress(MeasureIt.to_be_sent), (UDP_IP, UDP_PORT) )
                     #   print "sent", MeasureIt.to_be_sent
                        #print len(zlib.compress(MeasureIt.to_be_sent))
                        MeasureIt.to_be_sent = "[ %s," % (item_json,)
                    else:
                        MeasureIt.to_be_sent =  "%s%s," %(MeasureIt.to_be_sent, item_json)
               #     print MeasureIt.to_be_sent
                    MeasureIt.queue.task_done()
            except:
                import sys
                print sys.exc_info()
                pass
    sendOutIfFull = staticmethod(sendOutIfFull)


#    def addCacheHit(key, format, hit):
#        MeasureIt.queue.put(['CG', key, format, hit, socket.gethostname()])
#        MeasureIt.sendOutIfFull()
#    addCacheHit = staticmethod(addCacheHit)

    def addPageHit(time, path, view, get, response, pre_mw_time, view_time, post_mw_time, db_queries_time, db_routines_time):
        MeasureIt.queue.put([time, path, view[0], view[1], get, response, float(pre_mw_time), float(view_time), float(post_mw_time), float(db_queries_time), float(db_routines_time), socket.gethostname()])
        MeasureIt.sendOutIfFull()
    addPageHit = staticmethod(addPageHit)


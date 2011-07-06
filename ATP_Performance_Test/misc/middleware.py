from datetime import datetime
import cProfile
import os
import StringIO

class InstrumentMiddleware(object):
    def process_request(self, request):
        if 'profile' in request.REQUEST:
            request.profiler = cProfile.Profile()
            request.profiler.enable()

    def process_response(self, request, response):
        if hasattr(request, 'profiler'):
            request.profiler.disable()
            stamp = (request.META['REMOTE_ADDR'], datetime.now())
            request.profiler.dump_stats('/tmp/%s-%s.pro' % stamp)
            import pstats
            stream = StringIO.StringIO()
            stats = pstats.Stats('/tmp/%s-%s.pro' % stamp, stream=stream)
#            stats.strip_dirs()
            stats.sort_stats('time')
            stats.print_stats(12)
            stats.print_callers(12)
            stats.print_callees(12)
            os.remove('/tmp/%s-%s.pro' % stamp)
            response._container[0] += "<pre>"+stream.getvalue()+"</pre>"
            stream.close()
        return response
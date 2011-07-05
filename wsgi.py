import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ATP_Performance_Test.settings'
os.environ['ATP_HOST'] = 'DOTCLOUD'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

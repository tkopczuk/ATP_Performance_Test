import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'ATP_Performance_Test.settings'
os.environ['ATP_HOST'] = 'DOTCLOUD'

ALLDIRS = [os.path.join(os.path.dirname(os.path.abspath(__file__)), "ATP_Performance_test/")]

for directory in ALLDIRS:
      sys.path.insert(0, directory)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

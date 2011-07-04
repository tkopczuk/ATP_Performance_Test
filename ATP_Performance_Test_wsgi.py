import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'ATP_Performance_Test.settings'

import django.core.handlers.wsgi
    
application = django.core.handlers.wsgi.WSGIHandler()

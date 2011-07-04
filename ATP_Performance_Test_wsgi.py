import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'ATP_Performance_Test.settings'

import django.core.handlers.wsgi
    
application = django.core.handlers.wsgi.WSGIHandler()

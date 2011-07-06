#!/bin/sh

uwsgi --close-on-exec --disable-logging -p 2 -s /tmp/uwsgi.sock -H local_venv/ --pythonpath `pwd`/ -w ATP_Performance_Test.ATP_Performance_Test_wsgi

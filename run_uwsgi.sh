#!/bin/sh

uwsgi -p 1 -s /tmp/uwsgi.sock -H local_venv/ --pythonpath `pwd`/ -w ATP_Performance_Test.ATP_Performance_Test_wsgi 

#!/bin/sh

cd ATP_Performance_Test
gunicorn_django -w 1 -b unix:/tmp/uwsgi.sock 

#!/bin/sh

cd ATP_Performance_Test
gunicorn_django -w 2 -b unix:/tmp/gunicorn.sock

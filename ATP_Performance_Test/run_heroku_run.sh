#!/bin/bash
cd ATP_Performance_Test
. ../bin/activate
../bin/gunicorn_django -b 0.0.0.0:$PORT

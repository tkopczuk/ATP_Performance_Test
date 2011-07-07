#!/bin/bash
. bin/activate
pip -E . install --upgrade gunicorn
cd ATP_Performance_Test
../bin/gunicorn_django -b 0.0.0.0:$PORT -w 9

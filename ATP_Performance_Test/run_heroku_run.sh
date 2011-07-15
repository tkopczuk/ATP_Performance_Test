#!/bin/bash
. bin/activate
cd ATP_Performance_Test
python manage.py runserver 0.0.0.0:$PORT

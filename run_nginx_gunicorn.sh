#!/bin/sh
mkdir -p log/
mkdir -p logs/
nginx -p `pwd`/ -c etc/nginx_gunicorn.conf

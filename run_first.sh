#!/bin/sh
easy_install virtualenv
virtualenv local_venv
source local_venv/bin/activate
easy_install pip
pip install -r requirements.txt

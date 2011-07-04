#!/bin/bash
rm -r bin
rm -r include
rm -r lib
mkdir tmp
pip install -E tmp/bundle -r requirements.txt
mv tmp/bundle/* .
rm -r tmp/bundle


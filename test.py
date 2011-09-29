import os, sys

ALLDIRS = [os.path.join(os.path.dirname(os.path.abspath(__file__)), "ATP_Performance_test/")]

for directory in ALLDIRS:
      sys.path.insert(0, directory)
import askthepony.middleware

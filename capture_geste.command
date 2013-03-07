#!/usr/bin/env python
import sys, os
dir1 = os.path.join(os.path.dirname(sys.argv[0]))
os.chdir(dir1)
exec(open('start.py').read())

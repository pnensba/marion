#!/Library/Frameworks/Python.framework/Versions/Current/bin/python2.7
import sys, os
dir1 = os.path.join(os.path.dirname(sys.argv[0]))
os.chdir(dir1)
exec(open('plot.py').read())

#!/usr/bin/env python3
# -*- mode:python;coding:utf-8;python-indent:2 -*-
import sys, os
dir1 = os.path.join(os.path.dirname(sys.argv[0]))
os.chdir(dir1)
exec(open('surtitre.py').read())
# execfile('surtitre.py')

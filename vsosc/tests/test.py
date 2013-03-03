# -*- mode: python; coding: utf-8 ; python-indent: 2 -*-
import sys
sys.path.append('../..') # directory where vsosc stands
import vsosc

# create a test function
def test(msg):
    print (msg)

# create a receiver
r = vsosc.Receiver('127.0.0.1', 9001)
r.bind("/test",test)

# create a sender
s = vsosc.Sender('127.0.0.1', 9001)
s.send('/test', 'ceci est un premier test',1)

s_pd = vsosc.Sender('127.0.0.1', 9002)
s_pd.send('/test', '/from_py', 'ceci est un premier test',1)

s_sc = vsosc.Sender('127.0.0.1', 57120)
s_sc.send('/test', 'ceci est un premier test',1)

# limited to 9000 chars

# if you want to send tuples do:
s.send('/test', *[5,78])
# not:
# s.send('/test', [5,78])

import platform
PY3 = (platform.python_version_tuple()[0]=='3')
if PY3:
    a = input('Press Return to quit...\n')
else:
    a = raw_input('Press Return to quit...\n')

r.quit()
s.quit()

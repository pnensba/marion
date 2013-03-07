#!/Library/Frameworks/Python.framework/Versions/Current/bin/python2.7
import os, sys, traceback
import subprocess, time
import vsosc
from numpy import *

path = "/Applications/Pd-extended.app/Contents/Resources/bin/pdextended"
#sub = subprocess.Popen([path, '-path liken', 'capteurs_midi.pd'])
sub = subprocess.Popen(path+' -path liken -mididev 1 capteurs_midi.pd', shell=True)

global time0, recording, a
recording = False
time0 = 0
a = [[],[],[],[]]

def capteurs(*v):
  global recording, time0, a
  val = v[0]
  if recording: 
    a[0].append(time.time()-time0)
    a[1].append(val[0])
    a[2].append(val[1])
    a[3].append(val[2])

def trigger(*v):
  global recording, time0, a
  val = v[0][0]
  if val == 1:
    print'rec'
    time0 = time.time()
    recording = True
    a = [[],[],[],[]]
  else: 
    print 'stop'
    savetxt('test.txt', array(a))

r = vsosc.Receiver('127.0.0.1', 9001)
r.bind('/pd/capts', capteurs)
r.bind('/pd/capt_bin', trigger)

try: 
   while True: time.sleep(1)
except:
  info = sys.exc_info()
  trace = info[2]
  traceback.print_tb(trace)
  r.quit()
  sys.exit(0)
# -*- mode: python; coding: utf-8 ; python-indent: 2 -*-
"""
simple interface to  V2_Lab Osc implementation
GPL Vincent Rioux
0.1 : in zz_old (use own thread)
0.2 2009 : use thread from v2 implementation
0.3 100418 : python3 compatible
0.4 100728 : liblo compatible
0.5 100802 : removed init
0.6 110726 : refactored with fresh code from v2 => now should work with python3
0.7 111120 : using new code from v2 (python2 and python3)
0.8 120121 : fixed pbs with quitting receivers (using thread.join function)
0.9 121226 : automatically encode strings in utf8 with unicode-escape sequences
"""

import platform, gc
PY3 = (platform.python_version_tuple()[0]=='3')

TRYLIBLO = False

if TRYLIBLO:
  try: 
    import liblo
    LIBLO = True
    print("LIBLO detected - will be used")
  except: LIBLO  = False
else:
  LIBLO = False
  print("Not trying to use LIBLO")

if not LIBLO:
  if PY3: 
    try: import OSC3 as OSC
    except: exec("from . import OSC3 as OSC")
  else: import OSC
  
import socket
from threading import Thread

class Sender:
  def __init__(self, ipAddr='127.0.0.1', port = 9001):
    self.ipAddr = ipAddr
    self.port = int(port)
    self.addr = (ipAddr, port)
    if not LIBLO: self.osc = OSC.OSCClient()
    self.connect()

  def connect(self):
    if LIBLO: 
      #addr = 'osc.tcp://%s:%d'%self.addr
      addr = 'osc.udp://%s:%d'%self.addr
      print(addr)
      self.osc = liblo.Address(addr)
    else: self.osc.connect(self.addr)
        
  def init(self): pass

  def send(self, addr='/null', *args):
    if LIBLO: msg = liblo.Message(addr)
    else: msg = OSC.OSCMessage(); msg.setAddress(addr)

    for arg in args:
      if type(arg)==type(""):
        if PY3: arg = arg.encode('unicode-escape').decode('ascii')
        else: arg = unicode(arg,'utf-8').encode('unicode-escape').decode('ascii')
      if LIBLO: msg.add(arg)
      else: msg.extend(arg)

    if LIBLO: liblo.send(self.osc, msg)
    else: self.osc.send(msg)

  def sendpd(self,addr='/null', *args):
    args=args+('',)
    self.send(addr,*args)

  def close(self):
    self.quit()

  def quit(self):
    if not LIBLO: self.osc.close()

################################ receive osc from The Other.
class rcvFunc:
  def __init__(self, func):
    self.func = func
  def __call__(self, *a):
    print (a)

class Receiver:
  def __init__(self, ipAddr='127.0.0.1', port = 9001) :
    self.ipAddr = ipAddr
    self.port = port
    self.addr = (ipAddr, port)
    self.tags = set()

    if LIBLO:
      #self.t = liblo.ServerThread(port, proto=liblo.TCP)
      self.t = liblo.ServerThread(port, proto=liblo.UDP)
    else:
      self.osc = OSC.ThreadingOSCServer(self.addr)
      self.t = Thread(target=self.osc.serve_forever)

    self.t.start()

  def init(self): pass
  def listen(self): self.init()

  def close(self):
    self.quit()

  def quit(self):
    if LIBLO: self.t.stop(); self.t.free(); gc.collect()
    else: self.osc.running = False; self.t.join(); self.osc.close(); 
      
  def add(self, func, tag):
    if tag in self.tags: return
    if LIBLO: self.t.add_method(tag,None, lambda *f: func(f[1]))
    else: self.osc.addMsgHandler(tag, lambda *f: func(f[2]))
    self.tags.add(tag)

  def bind(self, tag,func): self.add(func, tag)
    
  def unbind(self, tag):
    if tag not in self.tags: return
    if LIBLO: pass # self.t.del_method(tag, None)
    else: self.osc.delMsgHandler(tag) 
    self.tags.remove(tag)

  def remove(self, tag): self.unbind(tag)

  def unbind_all(self):
    for tag in list(self.tags): self.unbind(tag)

if __name__=='__main__':
  import time, sys, traceback
  print ("Use ctrl-C to quit.")
  
  def test(*msg):
    print (msg)

  r = Receiver()
  r.bind('/test', test)
  s = Sender()
  s.send('/test', 'it works!', 22)
  time.sleep(1)
  if 0:
    try: 
      while True: time.sleep(1)
    except:
      info = sys.exc_info()
      trace = info[2]
      # print info, trace
      traceback.print_tb(trace)

      print ('exit')
      r.quit()
      s.quit()
      sys.exit(0)

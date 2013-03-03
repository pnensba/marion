q = q ? ();
q.to_pd = NetAddr.new("127.0.0.1", 9002); // osc to puredata
q.to_py = NetAddr.new("127.0.0.1", 9001); // osc to python

q.osc_resp = OSCresponder(nil, '/test', {|time, resp, msg|
  msg.postln;
}
).add; // do not forget to add the responder!


// send to pd
q.to_pd.sendMsg("/test/from_sc","what's in a bird?", 45);
// send to python
q.to_py.sendMsg("/test","what's in a python egg?", 22);

// with a delay
q.to_py.sendBundle(3000, ["/test","pourquoi pas?", 45]);

q.to_pd.sendBundle(3000, ["/test/from_sc","pourquoi pas?", 45]);





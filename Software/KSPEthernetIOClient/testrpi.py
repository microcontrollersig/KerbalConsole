#!/usr/bin/env python3

import krpc

conn = krpc.connect(name='krpc test', address='192.168.20.107', rpc_port=50000, stream_port=50001)
control = conn.space_center.active_vessel.control
#print(control.sas)
#print(control.rcs)
control.sas = True
control.rcs = True

#!/usr/bin/env python3

'''
IMPORTANT:

In the game
------------------------

Install krpc mod  from  https://github.com/kylewill0725/krpc/releases and copy krpc folder into GameData

When you open a saved game in KSP, the krpc GUI dialog will open. 

Click Add Server, change Address to Any, click Save, then Start.
If all is well, green color next to Default Server, and icon on right hand side toolbar goes green.
You can close the dialog box.


On the PC running the game
------------------------------

You need to open the following inbound ports in the firewall of your PC (or turn off firewall)

TCP port 50000
TCP port 50001


On the Pi
-----------
on command line, run:

pip3 install krpc


replace the address below with the IP address of the PC

'''

import krpc

conn = krpc.connect(name='krpc test', address='192.168.20.107')
control = conn.space_center.active_vessel.control
#print(control.sas)
#print(control.rcs)
control.sas = True
control.rcs = True

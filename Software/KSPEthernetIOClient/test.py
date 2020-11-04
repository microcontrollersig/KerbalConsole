import krpc

'''
Install python 3.
Run this on the same PC as KSP.

Install krpc server mod from here 

https://github.com/kylewill0725/krpc/releases

Just need the file called krpc_waffle_edition-0.4.9.2.zip, unzip and put krpc folder in GameData

To install krpc python client, run from command prompt:

pip install krpc

or

python -m pip install krpc

'''

conn = krpc.connect(name='krpc test')
control = conn.space_center.active_vessel.control
#print(control.sas)
#print(control.rcs)
control.sas = True
control.rcs = True

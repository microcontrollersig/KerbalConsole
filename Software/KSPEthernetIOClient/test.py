import krpc

conn = krpc.connect(name='krpc test')
control = conn.space_center.active_vessel.control
#print(control.sas)
#print(control.rcs)
control.sas = True
control.rcs = True

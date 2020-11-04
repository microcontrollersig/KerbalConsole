import krpc

conn = krpc.connect(name='Mohan')
control = conn.space_center.active_vessel.control
#print(control.sas)
#print(control.rcs)
control.sas = True
control.rcs = True

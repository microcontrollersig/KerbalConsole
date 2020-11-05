
from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from time import sleep
import krpc

IPADDRESS = '192.168.20.107'

class KSP(QObject):
    connected = QtCore.pyqtSignal(bool)
    statusReport = QtCore.pyqtSignal(dict)

    def __init__(self, worker):
        super(KSP, self).__init__()        
        self.connection = None
        self._worker = worker
        self.connected.connect(self._worker.isConnected)
        self.statusReport.connect(self._worker.statusReport)

    def makeConnection(self):
        try:
            print("Attempting to make connection........")
            #self.connection = krpc.connect(address=IPADDRESS, name="Mohan's GUI Test Program")
            self.connection = krpc.connect(name="Mohan's GUI Test Program")
            self.connected.emit(True)        
        except:
            self.connected.emit(False)

    def disconnect(self):
        print("Connection about to be broken....")
        self.connection.close()
        self.connected.emit(False)

    def isConnected(self):
        return self.connection != None

    
    def updateSAS(self, val):
        control = self.connection.space_center.active_vessel.control
        control.sas = val

    
    def updateRCS(self, val):
        control = self.connection.space_center.active_vessel.control
        control.rcs = val
    

    @QtCore.pyqtSlot()    
    def reportFromKSP(self):
        while True:
            if self.connection != None:
                data = self.getData()
                self.statusReport.emit(data)
            sleep(0.5)

    def getData(self):
        if self.connection != None:
            control = self.connection.space_center.active_vessel.control
            return {'sas': control.sas, 'rcs': control.rcs}        
        

class Worker(QObject):
    sasChanged = QtCore.pyqtSignal(bool)
    rcsChanged = QtCore.pyqtSignal(bool)    
    reportKSP = QtCore.pyqtSignal()
    connectKSP = QtCore.pyqtSignal()
    disconnectKSP = QtCore.pyqtSignal()    
    connectedStatus = QtCore.pyqtSignal(bool)
    latestData = QtCore.pyqtSignal(dict)

    def __init__(self, ui):
        super(Worker, self).__init__()
        self.ui = ui
        self.connectedStatus.connect(self.ui.connectionStatusChanged)
        self.latestData.connect(self.ui.latestData)
        self.createKSPThread()

    def createKSPThread(self):
        self._ksp = KSP(self)
        self._ksp_thread = QtCore.QThread()
        self.sasChanged.connect(self._ksp.updateSAS)
        self.rcsChanged.connect(self._ksp.updateRCS)
        self.reportKSP.connect(self._ksp.reportFromKSP)
        self.connectKSP.connect(self._ksp.makeConnection)
        self.disconnectKSP.connect(self._ksp.disconnect)      
        self._ksp.moveToThread(self._ksp_thread)
        self._ksp_thread.start()
        self.reportKSP.emit()

    def run(self):
        print("Listening for data from KSP")
        pass

    @QtCore.pyqtSlot()     
    def makeConnection(self):
        self.connectKSP.emit()

    def disconnectConnection(self):
        self.disconnectKSP.emit()

    @QtCore.pyqtSlot(bool)
    def isConnected(self, val):
        self.connectedStatus.emit(val)

    @QtCore.pyqtSlot(bool)
    def updateSAS(self, sas):
        print(f"sas enters worker: {sas}")
        self.sasChanged.emit(sas)
        
    @QtCore.pyqtSlot(bool)
    def updateRCS(self, rcs):
        print(f"rcs enters worker: {rcs}")
        self.rcsChanged.emit(rcs)

    @QtCore.pyqtSlot(dict)
    def statusReport(self, status):
        self.latestData.emit(status)

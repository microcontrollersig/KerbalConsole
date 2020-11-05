
from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from time import sleep
import krpc

IPADDRESS = '192.168.20.107'

class KSP(QObject):
    def __init__(self):
        super(KSP, self).__init__()        
        self.connection = None

    def makeConnection(self):
        try:
            print("Attempting to make connection...")
            self.connection = krpc.connect(address=IPADDRESS, name="Mohan's GUI Test Program")
        except:
            pass

    def disconnect(self):
        self.connection.close()

    def isConnected(self):
        return self.connection != None

    @QtCore.pyqtSlot(bool)    
    def updateSAS(self, val):
        print(f"update sas: {val}")

    @QtCore.pyqtSlot()    
    def reportFromKSP(self):
        while True:
            sleep(1)

class Worker(QObject):
    sasChanged = QtCore.pyqtSignal(bool)
    reportKSP = QtCore.pyqtSignal()
    connectKSP = QtCore.pyqtSignal()

    def __init__(self):
        super(Worker, self).__init__()
        self.createKSPThread()

    def createKSPThread(self):
        self._ksp = KSP()
        self._ksp_thread = QtCore.QThread()
        self.sasChanged.connect(self._ksp.updateSAS)
        self.reportKSP.connect(self._ksp.reportFromKSP)
        self.connectKSP.connect(self._ksp.makeConnection)
        self._ksp.moveToThread(self._ksp_thread)
        self._ksp_thread.start()
        self.reportKSP.emit()

    def run(self):
        print("Listening for data from KSP")
        pass

    @QtCore.pyqtSlot()     
    def makeConnection(self):
        self.connectKSP.emit()

    @QtCore.pyqtSlot(bool)
    def updateSAS(self, sas):
        print(f"SAS value: {sas}")
        self.sasChanged.emit(sas)


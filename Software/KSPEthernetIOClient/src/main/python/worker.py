
from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from time import sleep

class KSP(QObject):
    def __init__(self):
        super(KSP, self).__init__()        

    @QtCore.pyqtSlot(bool)    
    def updateSAS(self, val):
        print(f"update sas: {val}")

class Worker(QObject):
    sasChanged = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(Worker, self).__init__()
        self.createKSPThread()

    def createKSPThread(self):
        self._ksp = KSP()
        self._ksp_thread = QtCore.QThread()
        self.sasChanged.connect(self._ksp.updateSAS)
        self._ksp.moveToThread(self._ksp_thread)
        self._ksp_thread.start()        

    def run(self):
        print("Listening for data from KSP")
        pass

    @QtCore.pyqtSlot(bool)
    def updateSAS(self, sas):
        print(f"SAS value: {sas}")
        self.sasChanged.emit(sas)


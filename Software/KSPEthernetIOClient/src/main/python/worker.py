
from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from time import sleep

class Worker(QObject):
    def __init__(self):
        super(Worker, self).__init__()
    
    def run(self):
        print("Listening for data from KSP")

    @QtCore.pyqtSlot(bool)
    def updateSAS(self, sas):
        print(f"SAS value: {sas}")


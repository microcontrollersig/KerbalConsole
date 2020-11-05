from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow,QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtCore
import sys
from worker import Worker

'''
class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Buttons/mainwindow.ui', self)

        self.show()
'''

form_1, base_1 = uic.loadUiType('Buttons/mainwindow.ui')

class Ui(base_1, form_1):
    sasUpdate = QtCore.pyqtSignal(bool)
    rcsUpdate = QtCore.pyqtSignal(bool)
    connectKSP = QtCore.pyqtSignal()
    disconnectKSP = QtCore.pyqtSignal()
    

    def __init__(self):
        super(base_1, self).__init__()
        self.setupUi(self)
        #print(self.centralWidget().findChild(QPushButton, "pushButtonConnect"))
        #print(self.pushButtonConnect.text())
        
        self._isConnected = False
        self._isConnecting = False
        self._sas = False
        self._rcs = False

        self.createWorkerThread()

        self.pushButtonConnect.clicked.connect(self.connectClicked)
        self.pushButtonSAS.clicked.connect(self.SASClicked)
        self.pushButtonRCS.clicked.connect(self.RCSClicked)

    def createWorkerThread(self):
        self._worker = Worker(self)
        self._worker_thread = QtCore.QThread()
        #self._worker_thread.started.connect(self._worker.run)
        self._worker.moveToThread(self._worker_thread)
        self._worker_thread.start()
        self.sasUpdate.connect(self._worker.updateSAS)
        self.connectKSP.connect(self._worker.makeConnection)
        self.disconnectKSP.connect(self._worker.disconnectConnection)
        self.sasUpdate.emit(False)

    def connectClicked(self):
        if not self._isConnected:
            self.connectionStatus.setText('Attempting to connect. Please be patient....')
            self.connectKSP.emit()
        else:
            self.connectionStatus.setText('Attempting to disconnect. Please wait...')
            self.disconnectKSP.emit()
        
    @QtCore.pyqtSlot(bool)       
    def connectionStatusChanged(self, val):
        if val:
            self.connectionStatus.setText("Connected. Fire away!")
            self._isConnected = True
            self.pushButtonConnect.setText("Disconnect")
            print("Connection successful.")
        else:
            self.connectionStatus.setText("Server Not Connected. Start KSP.")
            self._isConnected = False
            self.pushButtonConnect.setText("Connect")
            print("Connection not successful")


    def sendSASMessage(self, newSASValue):
        sas = 'ON' if newSASValue else 'OFF'
        print(f"SAS New Value sent to server: {sas}")

    def sendRCSMessage(self, newRCSValue):
        rcs = 'ON' if newRCSValue else 'OFF'
        print(f"RCS New Value sent to server: {rcs}")

    def SASClicked(self):
        sas = not self._sas
        self._sas = sas
        self.sendSASMessage(sas)
        self.updateCss()

    def RCSClicked(self):
        rcs = not self._rcs
        self._rcs = rcs
        self.sendRCSMessage(rcs)
        self.updateCss()

    def updateCss(self):
        sasColor = 'green' if self._sas else 'red'
        rcsColor = 'green' if self._rcs else 'red'
        
        newCss=''
        
        if self._sas:
          newCss += self.produceCssFragment("pushButtonSAS", sasColor)
        else:
           newCss += self.produceCssFragment("pushButtonSAS", sasColor)

        if self._rcs:
          newCss += self.produceCssFragment("pushButtonRCS", rcsColor)
        else:
           newCss += self.produceCssFragment("pushButtonRCS", rcsColor)

  
        self.setStyleSheet(newCss)


    def produceCssFragment(self, name, color):
        return f"""QPushButton#{name},QPushButton#pushButtonRCS {{
    color: #333;
    border: 5px solid {color};
    border-radius: 50px;
    padding: 5px;
    background: qradialgradient(
        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
        radius: 1.35, stop: 0 #fff, stop: 1 #bbb
        );
    }}

     """
if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = Ui()
    #window = QMainWindow()
    window.resize(620,600)
    window.setWindowFlags(
        Qt.Window |
        Qt.CustomizeWindowHint |
        Qt.WindowTitleHint |
        Qt.WindowCloseButtonHint |
        Qt.WindowStaysOnTopHint    
    )
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
    
    

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QMainWindow
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal, pyqtSlot
from PyQt5 import uic, QtGui

class Worker(QObject):
    newParams = pyqtSignal()

    @pyqtSlot()
    def paramUp(self):
        x=1
        for x in range(100):
            time.sleep(2)
            self.newParams.emit()
            print ("sent new params")
            x +=1

Ui_somewindow, _ = uic.loadUiType("mainwindow.ui") #the path to UI

class SomeWindow(QMainWindow, Ui_somewindow, QDialog):

    def __init__(self):

        QMainWindow.__init__(self)
        Ui_somewindow.__init__(self)
        self.setupUi(self)

        # Start custom functions
        self.params = {}
        self.pushButton.clicked.connect(self.complex) #NumEvent

    def complex(self):
        self.work = Worker()
        self.thread = QThread()
        self.thread.started.connect(self.worker.work)  # <--new line, make sure work starts.
        self.thread.start()
        self.work.newParams.connect(self.changeTextEdit)
        self.work.moveToThread(self.thread)
        self.thread.start()

        self.CustomComplexFunction()

    def CustomComplexFunction(self):
        self.params['City'] = 'Test'

    def changeTextEdit(self):

        try:
            City = self.params['City']
            self.textEdit_14.setPlainText(City)
        except KeyError:
            City = None
if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = SomeWindow()
    window.show()
    sys.exit(app.exec_())
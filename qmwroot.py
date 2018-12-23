'''
ColourApp/qmwroot.py
QMWRoot
By:
* Ken Shibata, Dec 2018
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qmwroot_ui import *
import sys

class QMWRoot(Ui_QMWRoot, QMainWindow):
    def __init__(self, QApp):
        super().__init__()

        self.QApp = QApp
    def finalUi(self):
        self.setupUi(self)
    def startUi(self):
        self.finalUi()
        self.show()

if __name__ == '__main__':
    QApp = QApplication(sys.argv)
    QMWRootInst = QMWRoot(QApp)
    QMWRootInst.startUi()
    sys.exit(QApp.exec_())
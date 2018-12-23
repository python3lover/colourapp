'''
ColourApp/qmwroot.py
QMWRoot
By:
* Ken Shibata, Dec 2018
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qmwroot_ui import *

def QMWRoot(Ui_QMWRoot, QMainWindow):
    def __init__(self, QApp):
        super().__init__()

        self.QApp = QApp
    def setupUi(self):
        self.setupUi(self)
    def startUi(self):
        self.setupUi()
        self.show()
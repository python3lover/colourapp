'''
ColourApp/qmwroot.py
QMWRoot
By:
* Ken Shibata, Dec 2018
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qmwroot_ui import *
import os, sys

class QMWRoot(Ui_QMWRoot, QMainWindow): # TODO Add support for showing apps from ~/Apps.
    def __init__(self, QApp):
        super().__init__()

        self.QApp = QApp
    def finalUi(self):
        self.setupUi(self)
    def updateUiLoadApps(self):
        appsDir = os.path.join(os.path.userexpand(), 'Apps')
        old_wd = os.cwd()
        os.chdir(appsDir)
        os.listdir()
        os.chdir(old_wd)

    def startUi(self):
        self.finalUi()
        self.show()

if __name__ == '__main__':
    QApp = QApplication(sys.argv)
    QMWRootInst = QMWRoot(QApp)
    QMWRootInst.startUi()
    sys.exit(QApp.exec_())
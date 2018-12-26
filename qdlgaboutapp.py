'''
ColourApp/qdlgaboutapp.py
QDlgAboutApp
By:
* Ken Shibata, Dec 2018
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qdlgaboutapp_ui import *
import os, sys, files

class QDlgAboutApp(Ui_QDlgAboutApp, QDialog):
    def __init__(self, QApp):
        super().__init__()

        self.QApp = QApp
    def finalUi(self):
        self.setupUi(self)
    def startUi(self):
        self.finalUi()
        self.show()

def auto(QApp):
    QDlgAboutAppInst = QDlgAboutApp(QApp)
    QDlgAboutAppInst.startUi()
    return QDlgAboutAppInst

if __name__ == '__main__':
    QApp = QApplication(sys.argv)
    QDlgAboutAppInst = QDlgAboutApp(QApp)
    QDlgAboutAppInst.startUi()
    sys.exit(QApp.exec_())
'''
ColourApp/qdlggeturl.py
QDlgGetURL
By:
* Ken Shibata, Dec 2018
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qdlggeturl_ui import *
import sys

class QDlgGetURL(Ui_QDlgGetURL, QDialog):
    def __init__(self, QApp):
        super().__init__()

        self.QApp = QApp
        self.URL = None
    def finalUi(self):
        self.setupUi(self)
        self.QPBCancel.clicked.connect(self.updateUiQActCancel)
        self.QPBOk.clicked.connect(self.updateUiQActOk)
    def updateUiQActCancel(self):
        self.URL = False
        self.path = False
        self.close()
    def updateUiQActOk(self):
        self.URL = self.QLEURL.text()
        self.path = self.QLEPath.text()
        self.close()
    def startUi(self):
        self.finalUi()
        self.exec_()
        return self.URL, self.path

def auto(QApp):
    QDlgGetURLInst = QDlgGetURL(QApp)
    print(QDlgGetURLInst.startUi())
    return QDlgGetURLInst, QDlgGetURLInst.URL

if __name__ == '__main__':
    QApp = QApplication(sys.argv)
    QDlgGetURLInst = QDlgGetURL(QApp)
    print(QDlgGetURLInst.startUi())
    sys.exit(QApp.exec_())
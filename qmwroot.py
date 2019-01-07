'''
ColourApp/qmwroot.py
QMWRoot
By:
* Ken Shibata, Dec 2018
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qmwroot_ui import *
from qdlgaboutapp import *
from qdlggeturl import *
import core, download
import os, sys, files, requests, io, zipfile

class QMWRoot(Ui_QMWRoot, QMainWindow):
    def __init__(self, QApp):
        super().__init__()

        self.QApp = QApp
    def finalUi(self):
        self.setupUi(self)
        self.QActAboutApp.triggered.connect(self.updateUiAboutApp)
        self.QActAuto.triggered.connect(self.updateUiAppAuto)
    def updateUiAboutApp(self):
        print('updateUiAboutApp')
        Inst = QDlgAboutApp(self.QApp)
        Inst.startUi()
        print('done')
    def updateUiGetURL(self):
        print('updateUiGetURL')
        Inst = QDlgAboutApp(self.QApp)
        Inst.startUi()
        print('done')
    def updateUiAppAuto(self):
        Inst = QDlgGetURL(self.QApp)
        pack_url, pack_path = Inst.startUi()
        DInst = download.download(pack_url, pack_path)
        DInst.download()
        core.auto(pack_path)
    def updateUiLoadApps(self):
        appsDir = os.path.expanduser('~/Apps')
        try:
            tree = files.list_files(appsDir)
        except:
            return ['~/Apps not Found', 'ColourApp is not properly set in your system. Please create a directory called "~/Apps".']
        print(tree)
        items = files.tree_to_path(tree)
        print(items)
        for i in range(len(items[0])):
            QLWIItem = QListWidgetItem(items[0][i])
            QLWIItem.setToolTip(items[1][i])
            self.QLWApps.addItem(QLWIItem)
        return None
    def updateUiError(self, title, message):
        Inst = QMessageBox.critical(self, title, message, QMessageBox.Abort)
        Inst.show()
    def startUi(self):
        self.finalUi()
        code = self.updateUiLoadApps()
        if not code:
            self.updateUiError(*code)
        self.show()

if __name__ == '__main__':
    QApp = QApplication(sys.argv)
    QMWRootInst = QMWRoot(QApp)
    QMWRootInst.startUi()
    sys.exit(QApp.exec_())
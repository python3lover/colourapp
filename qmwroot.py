'''
ColourApp/qmwroot.py
QMWRoot
By:
* Ken Shibata, Dec 2018
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qmwroot_ui import *
import os, sys, files

class QMWRoot(Ui_QMWRoot, QMainWindow):
    def __init__(self, QApp):
        super().__init__()

        self.QApp = QApp
    def finalUi(self):
        self.setupUi(self)
    def updateUiLoadApps(self):
        appsDir = os.path.expanduser('~/Apps')
        tree = files.list_files(appsDir)
        print(tree)
        items = files.tree_to_path(tree)
        print(items)
        for i in range(len(items[0])):
            QLWIItem = QListWidgetItem(items[0][i])
            QLWIItem.setToolTip(items[1][i])
            self.QLWApps.addItem(QLWIItem)
    def startUi(self):
        self.finalUi()
        self.updateUiLoadApps()
        self.show()

if __name__ == '__main__':
    QApp = QApplication(sys.argv)
    QMWRootInst = QMWRoot(QApp)
    QMWRootInst.startUi()
    sys.exit(QApp.exec_())
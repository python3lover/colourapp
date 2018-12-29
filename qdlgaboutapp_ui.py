# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qdlgaboutapp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QDlgAboutApp(object):
    def setupUi(self, QDlgAboutApp):
        QDlgAboutApp.setObjectName("QDlgGetURL")
        QDlgAboutApp.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(QDlgAboutApp)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.QVLRoot = QtWidgets.QVBoxLayout()
        self.QVLRoot.setObjectName("QVLRoot")
        self.QHLTitle = QtWidgets.QHBoxLayout()
        self.QHLTitle.setObjectName("QHLTitle")
        self.QLbTitle = QtWidgets.QLabel(QDlgAboutApp)
        self.QLbTitle.setObjectName("QLbTitle")
        self.QHLTitle.addWidget(self.QLbTitle)
        self.QVLRoot.addLayout(self.QHLTitle)
        self.QLbName = QtWidgets.QLabel(QDlgAboutApp)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.QLbName.setFont(font)
        self.QLbName.setObjectName("QLbName")
        self.QVLRoot.addWidget(self.QLbName)
        self.QLbInfo = QtWidgets.QLabel(QDlgAboutApp)
        self.QLbInfo.setObjectName("QLbInfo")
        self.QVLRoot.addWidget(self.QLbInfo)
        self.QLbLicense = QtWidgets.QLabel(QDlgAboutApp)
        self.QLbLicense.setTextFormat(QtCore.Qt.RichText)
        self.QLbLicense.setObjectName("QLbLicense")
        self.QVLRoot.addWidget(self.QLbLicense)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.QVLRoot.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.QVLRoot)

        self.retranslateUi(QDlgAboutApp)
        QtCore.QMetaObject.connectSlotsByName(QDlgAboutApp)

    def retranslateUi(self, QDlgAboutApp):
        _translate = QtCore.QCoreApplication.translate
        QDlgAboutApp.setWindowTitle(_translate("QDlgGetURL", "Dialog"))
        self.QLbTitle.setText(_translate("QDlgGetURL", "About ColourApp"))
        self.QLbName.setText(_translate("QDlgGetURL", "ColourApp"))
        self.QLbInfo.setText(_translate("QDlgGetURL", "GUI 0.0.0 Stable en-ca"))
        self.QLbLicense.setText(_translate("QDlgGetURL", "<html><head/><body><p>ColourApp is licensed under the <a href=\"https://colourroot.github.io/License/\"><span style=\" text-decoration: underline; color:#0000ff;\">MIT License</span></a>.</p></body></html>"))


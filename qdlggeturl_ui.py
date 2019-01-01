# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qdlggeturl.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QDlgGetURL(object):
    def setupUi(self, QDlgGetURL):
        QDlgGetURL.setObjectName("QDlgGetURL")
        QDlgGetURL.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(QDlgGetURL)
        self.verticalLayout.setObjectName("verticalLayout")
        self.QVLRoot = QtWidgets.QVBoxLayout()
        self.QVLRoot.setObjectName("QVLRoot")
        self.QHLTitle = QtWidgets.QHBoxLayout()
        self.QHLTitle.setObjectName("QHLTitle")
        self.QLbTitle = QtWidgets.QLabel(QDlgGetURL)
        self.QLbTitle.setObjectName("QLbTitle")
        self.QHLTitle.addWidget(self.QLbTitle)
        self.QPBCancel = QtWidgets.QPushButton(QDlgGetURL)
        self.QPBCancel.setObjectName("QPBCancel")
        self.QHLTitle.addWidget(self.QPBCancel)
        self.QPBOk = QtWidgets.QPushButton(QDlgGetURL)
        self.QPBOk.setObjectName("QPBOk")
        self.QHLTitle.addWidget(self.QPBOk)
        self.QVLRoot.addLayout(self.QHLTitle)
        self.QLEURL = QtWidgets.QLineEdit(QDlgGetURL)
        self.QLEURL.setObjectName("QLEURL")
        self.QVLRoot.addWidget(self.QLEURL)
        self.QLEPath = QtWidgets.QLineEdit(QDlgGetURL)
        self.QLEPath.setObjectName("QLEPath")
        self.QVLRoot.addWidget(self.QLEPath)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.QVLRoot.addItem(spacerItem)
        self.verticalLayout.addLayout(self.QVLRoot)

        self.retranslateUi(QDlgGetURL)
        QtCore.QMetaObject.connectSlotsByName(QDlgGetURL)

    def retranslateUi(self, QDlgGetURL):
        _translate = QtCore.QCoreApplication.translate
        QDlgGetURL.setWindowTitle(_translate("QDlgGetURL", "Form"))
        self.QLbTitle.setText(_translate("QDlgGetURL", "Enter URL"))
        self.QPBCancel.setText(_translate("QDlgGetURL", "&Cancel"))
        self.QPBOk.setText(_translate("QDlgGetURL", "&Ok"))


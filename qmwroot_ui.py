# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qmwroot.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QMWRoot(object):
    def setupUi(self, QMWRoot):
        QMWRoot.setObjectName("QMWRoot")
        QMWRoot.resize(400, 300)
        self.QWgtCentral = QtWidgets.QWidget(QMWRoot)
        self.QWgtCentral.setObjectName("QWgtCentral")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.QWgtCentral)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.QVLRoot = QtWidgets.QVBoxLayout()
        self.QVLRoot.setSpacing(6)
        self.QVLRoot.setObjectName("QVLRoot")
        self.QLbApps = QtWidgets.QLabel(self.QWgtCentral)
        self.QLbApps.setObjectName("QLbApps")
        self.QVLRoot.addWidget(self.QLbApps)
        self.QLWApps = QtWidgets.QListWidget(self.QWgtCentral)
        self.QLWApps.setObjectName("QLWApps")
        self.QVLRoot.addWidget(self.QLWApps)
        self.verticalLayout_2.addLayout(self.QVLRoot)
        QMWRoot.setCentralWidget(self.QWgtCentral)
        self.QMBRoot = QtWidgets.QMenuBar(QMWRoot)
        self.QMBRoot.setGeometry(QtCore.QRect(0, 0, 400, 16))
        self.QMBRoot.setObjectName("QMBRoot")
        self.QMnControl = QtWidgets.QMenu(self.QMBRoot)
        self.QMnControl.setObjectName("QMnControl")
        self.QMnApp = QtWidgets.QMenu(self.QMBRoot)
        self.QMnApp.setObjectName("QMnApp")
        QMWRoot.setMenuBar(self.QMBRoot)
        self.QTBApp = QtWidgets.QToolBar(QMWRoot)
        self.QTBApp.setObjectName("QTBApp")
        QMWRoot.addToolBar(QtCore.Qt.TopToolBarArea, self.QTBApp)
        self.QSBRoot = QtWidgets.QStatusBar(QMWRoot)
        self.QSBRoot.setObjectName("QSBRoot")
        QMWRoot.setStatusBar(self.QSBRoot)
        self.QActExit = QtWidgets.QAction(QMWRoot)
        self.QActExit.setObjectName("QActExit")
        self.QActAboutApp = QtWidgets.QAction(QMWRoot)
        self.QActAboutApp.setObjectName("QActAboutApp")
        self.QActAboutOrg = QtWidgets.QAction(QMWRoot)
        self.QActAboutOrg.setObjectName("QActAboutOrg")
        self.QActDownload = QtWidgets.QAction(QMWRoot)
        self.QActDownload.setObjectName("QActDownload")
        self.QActUnpack = QtWidgets.QAction(QMWRoot)
        self.QActUnpack.setObjectName("QActUnpack")
        self.QActValidate = QtWidgets.QAction(QMWRoot)
        self.QActValidate.setObjectName("QActValidate")
        self.QActCopy = QtWidgets.QAction(QMWRoot)
        self.QActCopy.setObjectName("QActCopy")
        self.QActAuto = QtWidgets.QAction(QMWRoot)
        self.QActAuto.setObjectName("QActAuto")
        self.QMnControl.addAction(self.QActExit)
        self.QMnControl.addAction(self.QActAboutApp)
        self.QMnControl.addAction(self.QActAboutOrg)
        self.QMnApp.addAction(self.QActDownload)
        self.QMnApp.addAction(self.QActUnpack)
        self.QMnApp.addAction(self.QActValidate)
        self.QMnApp.addAction(self.QActCopy)
        self.QMnApp.addSeparator()
        self.QMnApp.addAction(self.QActAuto)
        self.QMBRoot.addAction(self.QMnControl.menuAction())
        self.QMBRoot.addAction(self.QMnApp.menuAction())
        self.QTBApp.addAction(self.QActDownload)
        self.QTBApp.addAction(self.QActUnpack)
        self.QTBApp.addAction(self.QActValidate)
        self.QTBApp.addAction(self.QActCopy)
        self.QTBApp.addSeparator()
        self.QTBApp.addAction(self.QActAuto)

        self.retranslateUi(QMWRoot)
        QtCore.QMetaObject.connectSlotsByName(QMWRoot)

    def retranslateUi(self, QMWRoot):
        _translate = QtCore.QCoreApplication.translate
        QMWRoot.setWindowTitle(_translate("QMWRoot", "QMWRoot"))
        self.QLbApps.setText(_translate("QMWRoot", "Apps"))
        self.QMnControl.setTitle(_translate("QMWRoot", "ColourApp UI"))
        self.QMnApp.setTitle(_translate("QMWRoot", "App"))
        self.QActExit.setText(_translate("QMWRoot", "&Exit"))
        self.QActAboutApp.setText(_translate("QMWRoot", "&About ColourApp"))
        self.QActAboutOrg.setText(_translate("QMWRoot", "A&bout ColourRoot"))
        self.QActDownload.setText(_translate("QMWRoot", "&Download"))
        self.QActUnpack.setText(_translate("QMWRoot", "&Unpack"))
        self.QActValidate.setText(_translate("QMWRoot", "&Validate"))
        self.QActCopy.setText(_translate("QMWRoot", "&Copy"))
        self.QActAuto.setText(_translate("QMWRoot", "&Automatic"))


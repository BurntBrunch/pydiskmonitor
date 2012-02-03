# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Feb  2 14:53:30 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(715, 501)
        MainWindow.setMinimumSize(QtCore.QSize(715, 501))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabPages = QtGui.QTabWidget(self.centralwidget)
        self.tabPages.setMinimumSize(QtCore.QSize(123, 0))
        self.tabPages.setObjectName(_fromUtf8("tabPages"))
        self.gridLayout.addWidget(self.tabPages, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuManager = QtGui.QMenu(self.menubar)
        self.menuManager.setObjectName(_fromUtf8("menuManager"))
        self.menuDevices = QtGui.QMenu(self.menubar)
        self.menuDevices.setObjectName(_fromUtf8("menuDevices"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.action_Add = QtGui.QAction(MainWindow)
        self.action_Add.setObjectName(_fromUtf8("action_Add"))
        self.action_Remove_current = QtGui.QAction(MainWindow)
        self.action_Remove_current.setObjectName(_fromUtf8("action_Remove_current"))
        self.menuManager.addAction(self.action_Quit)
        self.menuDevices.addAction(self.action_Add)
        self.menuDevices.addAction(self.action_Remove_current)
        self.menubar.addAction(self.menuManager.menuAction())
        self.menubar.addAction(self.menuDevices.menuAction())

        self.retranslateUi(MainWindow)
        self.tabPages.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Device Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.menuManager.setTitle(QtGui.QApplication.translate("MainWindow", "&Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDevices.setTitle(QtGui.QApplication.translate("MainWindow", "&Devices", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add.setText(QtGui.QApplication.translate("MainWindow", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Remove_current.setText(QtGui.QApplication.translate("MainWindow", "R&emove current", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Remove_current.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))


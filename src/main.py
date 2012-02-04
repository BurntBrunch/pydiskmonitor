#!/usr/bin/env python
# coding: utf-8
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from devices import DeviceManager, UDisksManager
from window import MainWindow

class Application(object):
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.initApp()
        self.initUi()

        sys.exit(self.app.exec_())
    
    def initApp(self):
        self.app.setOrganizationName("Delyan's")
        self.app.setOrganizationDomain("None")
        self.app.setApplicationName("Disk Watcher")

        self.dev_manager = DeviceManager()
        self.udisks_manager = UDisksManager(self.dev_manager)
        self.window = None

    def initUi(self):
        self.tray_icon = QSystemTrayIcon(self.app)
        self.icon = QIcon.fromTheme('drive-removable-media')
        self.tray_icon.setIcon(self.icon)
        self.tray_icon.activated.connect(self.tray_activated)
        self.tray_icon.setVisible(True)

        self.tray_menu = QMenu()
        self.tray_menu.addAction("&Show manager").triggered.connect(lambda:
                                                                    self.tray_activated(QSystemTrayIcon.DoubleClick))

        self.tray_menu.addAction("&Quit").triggered.connect(self.app.quit)
        self.tray_icon.setContextMenu(self.tray_menu)

    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.window is not None and self.window.isVisible():
                self.window.hide()
            else:
                self.window = MainWindow(self.dev_manager)
                self.window.show()

if __name__ == "__main__":
    app = Application()

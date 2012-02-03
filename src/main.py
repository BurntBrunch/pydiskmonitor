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

        # TEST
        self.tray_activated(QSystemTrayIcon.DoubleClick)

        sys.exit(self.app.exec_())
    
    def initApp(self):
        self.app.setOrganizationName("Delyan's")
        self.app.setOrganizationDomain("None")
        self.app.setApplicationName("Disk Watcher")

        self.dev_manager = DeviceManager()
        self.udisks_manager = UDisksManager(self.dev_manager)

    def initUi(self):
        self.tray_icon = QSystemTrayIcon(self.app)
        self.icon = QIcon.fromTheme('drive-removable-media')
        self.tray_icon.setIcon(self.icon)
        self.tray_icon.activated.connect(self.tray_activated)
        self.tray_icon.setVisible(True)

    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.Context:
            self.app.quit()
        elif reason == QSystemTrayIcon.DoubleClick:
            self.window = MainWindow(self.dev_manager)
            self.window.show()

if __name__ == "__main__":
    app = Application()

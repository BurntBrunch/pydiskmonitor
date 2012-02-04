from PyQt4.QtGui import *
from PyQt4.QtCore import *
from devices import DeviceManager
from ui_mainwindow import *
from ui_page import *

class MainWindow(QMainWindow):
    def __init__(self, manager):
        super(MainWindow, self).__init__()

        self.manager = manager

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon.fromTheme("drive-removable-media"))

        self.setupSignals()
        self.synchronize_pages()

    def setupSignals(self):
        self.ui.action_Quit.activated.connect(QApplication.quit)
        self.ui.action_Add.activated.connect(self.add_device)
        self.ui.action_Remove_current.activated.connect(self.remove_device)

    def add_device(self):
        dev = self.manager.new_device()
        self.manager.save_device(dev)

        self.synchronize_pages()
        self.ui.tabPages.setCurrentIndex(self.ui.tabPages.count()-1)

    def remove_device(self):
        dev = self.ui.tabPages.currentWidget().device

        self.manager.remove_device(dev)
        self.synchronize_pages()

    def synchronize_pages(self):
        self.ui.tabPages.clear()

        for dev in self.manager.devices.values():
            page = TabPage(dev)
            page.save_device.connect(self.save_device)

            self.ui.tabPages.addTab(page, dev['name'])

    def save_device(self):
        page = self.ui.tabPages.currentWidget()
        dev = page.device

        self.manager.save_device(dev)
        self.ui.tabPages.setTabText(self.ui.tabPages.currentIndex(), dev['name'])

class TabPage(QWidget):
    save_device = pyqtSignal()

    def __init__(self, device):
        super(TabPage, self).__init__()
        self.device = device
        
        self.ui = Ui_Page()
        self.ui.setupUi(self)
        self.setupSignals()

        self.fillData()

    def fillData(self):
        dev = self.device
        self.ui.name_text_edit.setPlainText(dev['name'])
        self.ui.exec_text_edit.setPlainText(dev['exec'])
        self.ui.rules_text_edit.setPlainText("\n".join(dev['rules']))
    
    def setupSignals(self):
        self.ui.save_button.clicked.connect(self.save_page)
        self.ui.reset_button.clicked.connect(self.fillData)

    def save_page(self):
        self.device['name'] = str(self.ui.name_text_edit.toPlainText()).strip()
        self.device['exec'] = str(self.ui.exec_text_edit.toPlainText()).strip()

        rules = str(self.ui.rules_text_edit.toPlainText()).strip().split("\n")
        rules = filter(lambda x: len(x) > 0, rules)
        self.device['rules'] = rules

        self.save_device.emit()

        self.fillData()
        



        


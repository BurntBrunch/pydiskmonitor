# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page.ui'
#
# Created: Thu Feb  2 16:32:20 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page(object):
    def setupUi(self, Page):
        Page.setObjectName(_fromUtf8("Page"))
        Page.resize(391, 339)
        self.formLayout = QtGui.QFormLayout(Page)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.rules_label = QtGui.QLabel(Page)
        self.rules_label.setObjectName(_fromUtf8("rules_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.rules_label)
        self.rules_text_edit = QtGui.QPlainTextEdit(Page)
        self.rules_text_edit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.rules_text_edit.setObjectName(_fromUtf8("rules_text_edit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.rules_text_edit)
        self.exec_label = QtGui.QLabel(Page)
        self.exec_label.setObjectName(_fromUtf8("exec_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.exec_label)
        self.exec_text_edit = QtGui.QPlainTextEdit(Page)
        self.exec_text_edit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.exec_text_edit.setObjectName(_fromUtf8("exec_text_edit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.exec_text_edit)
        self.save_button = QtGui.QPushButton(Page)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.save_button)
        self.reset_button = QtGui.QPushButton(Page)
        self.reset_button.setObjectName(_fromUtf8("reset_button"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.reset_button)
        self.name_label = QtGui.QLabel(Page)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.name_label)
        self.name_text_edit = QtGui.QPlainTextEdit(Page)
        self.name_text_edit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.name_text_edit.setObjectName(_fromUtf8("name_text_edit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.name_text_edit)

        self.retranslateUi(Page)
        QtCore.QMetaObject.connectSlotsByName(Page)

    def retranslateUi(self, Page):
        Page.setWindowTitle(QtGui.QApplication.translate("Page", "Page", None, QtGui.QApplication.UnicodeUTF8))
        self.rules_label.setText(QtGui.QApplication.translate("Page", "Rules:", None, QtGui.QApplication.UnicodeUTF8))
        self.exec_label.setText(QtGui.QApplication.translate("Page", "Exec:", None, QtGui.QApplication.UnicodeUTF8))
        self.save_button.setText(QtGui.QApplication.translate("Page", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_button.setText(QtGui.QApplication.translate("Page", "&Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate("Page", "Name:", None, QtGui.QApplication.UnicodeUTF8))


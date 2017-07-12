# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogDialog.ui'
#
# Created: Wed Jul 12 16:15:51 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_LogDialog(object):
    def setupUi(self, LogDialog):
        LogDialog.setObjectName("LogDialog")
        LogDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(LogDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(LogDialog)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi(LogDialog)
        QtCore.QMetaObject.connectSlotsByName(LogDialog)

    def retranslateUi(self, LogDialog):
        LogDialog.setWindowTitle(QtWidgets.QApplication.translate("LogDialog", "Dialog", None, -1))


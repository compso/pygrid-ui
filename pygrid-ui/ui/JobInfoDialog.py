# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JobInfoDialog.ui'
#
# Created: Tue Jul  4 17:13:13 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_JobInfoDialog(object):
    def setupUi(self, JobInfoDialog):
        JobInfoDialog.setObjectName("JobInfoDialog")
        JobInfoDialog.resize(833, 394)
        self.verticalLayout = QtWidgets.QVBoxLayout(JobInfoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(JobInfoDialog)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 809, 162))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 809, 161))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scrollArea_2)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(JobInfoDialog)
        QtCore.QMetaObject.connectSlotsByName(JobInfoDialog)

    def retranslateUi(self, JobInfoDialog):
        JobInfoDialog.setWindowTitle(QtWidgets.QApplication.translate("JobInfoDialog", "JobInfo (jobid)", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("JobInfoDialog", "Job Info", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("JobInfoDialog", "Task Info", None, -1))


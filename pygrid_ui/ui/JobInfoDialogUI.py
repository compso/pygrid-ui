# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JobInfoDialog.ui'
#
# Created: Wed Jul 12 16:15:50 2017
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
        self.jobInfo = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jobInfo.sizePolicy().hasHeightForWidth())
        self.jobInfo.setSizePolicy(sizePolicy)
        self.jobInfo.setMaximumSize(QtCore.QSize(16777215, 200))
        self.jobInfo.setObjectName("jobInfo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.jobInfo)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.jobInfo_scroll = QtWidgets.QScrollArea(self.jobInfo)
        self.jobInfo_scroll.setWidgetResizable(True)
        self.jobInfo_scroll.setObjectName("jobInfo_scroll")
        self.jobInfo_w = QtWidgets.QWidget()
        self.jobInfo_w.setGeometry(QtCore.QRect(0, 0, 809, 162))
        self.jobInfo_w.setObjectName("jobInfo_w")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.jobInfo_w)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.details_table = QtWidgets.QTableWidget(self.jobInfo_w)
        self.details_table.setAlternatingRowColors(True)
        self.details_table.setObjectName("details_table")
        self.details_table.setColumnCount(2)
        self.details_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.details_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.details_table.setHorizontalHeaderItem(1, item)
        self.details_table.horizontalHeader().setVisible(False)
        self.details_table.horizontalHeader().setStretchLastSection(True)
        self.details_table.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.details_table)
        self.jobInfo_scroll.setWidget(self.jobInfo_w)
        self.horizontalLayout.addWidget(self.jobInfo_scroll)
        self.taskInfo = QtWidgets.QGroupBox(self.splitter)
        self.taskInfo.setObjectName("taskInfo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.taskInfo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.taskInfo_scroll = QtWidgets.QScrollArea(self.taskInfo)
        self.taskInfo_scroll.setWidgetResizable(True)
        self.taskInfo_scroll.setObjectName("taskInfo_scroll")
        self.taskInfo_w = QtWidgets.QWidget()
        self.taskInfo_w.setGeometry(QtCore.QRect(0, 0, 809, 161))
        self.taskInfo_w.setObjectName("taskInfo_w")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.taskInfo_w)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.taskInfo_scroll.setWidget(self.taskInfo_w)
        self.horizontalLayout_2.addWidget(self.taskInfo_scroll)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(JobInfoDialog)
        QtCore.QMetaObject.connectSlotsByName(JobInfoDialog)

    def retranslateUi(self, JobInfoDialog):
        JobInfoDialog.setWindowTitle(QtWidgets.QApplication.translate("JobInfoDialog", "JobInfo (jobid)", None, -1))
        self.jobInfo.setTitle(QtWidgets.QApplication.translate("JobInfoDialog", "Job Info", None, -1))
        self.details_table.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("JobInfoDialog", "Key", None, -1))
        self.details_table.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("JobInfoDialog", "Value", None, -1))
        self.taskInfo.setTitle(QtWidgets.QApplication.translate("JobInfoDialog", "Task Info", None, -1))


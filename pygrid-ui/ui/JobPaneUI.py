# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JobPane.ui'
#
# Created: Thu Jul  6 17:44:02 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_JobPane(object):
    def setupUi(self, JobPane):
        JobPane.setObjectName("JobPane")
        JobPane.resize(519, 43)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(JobPane.sizePolicy().hasHeightForWidth())
        JobPane.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(JobPane)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainFrame = DetailsPane(JobPane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.id_label = QtWidgets.QLabel(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id_label.sizePolicy().hasHeightForWidth())
        self.id_label.setSizePolicy(sizePolicy)
        self.id_label.setObjectName("id_label")
        self.horizontalLayout_2.addWidget(self.id_label)
        self.owner_label = QtWidgets.QLabel(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.owner_label.sizePolicy().hasHeightForWidth())
        self.owner_label.setSizePolicy(sizePolicy)
        self.owner_label.setObjectName("owner_label")
        self.horizontalLayout_2.addWidget(self.owner_label)
        self.name_label = ElidedLabel(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setScaledContents(False)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_2.addWidget(self.name_label)
        self.queue_label = QtWidgets.QLabel(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.queue_label.sizePolicy().hasHeightForWidth())
        self.queue_label.setSizePolicy(sizePolicy)
        self.queue_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.queue_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.queue_label.setObjectName("queue_label")
        self.horizontalLayout_2.addWidget(self.queue_label)
        self.status_label = QtWidgets.QLabel(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setText("")
        self.status_label.setPixmap(QtGui.QPixmap(":/res/png/warning.png"))
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_2.addWidget(self.status_label)
        self.info_btn = QtWidgets.QPushButton(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_btn.sizePolicy().hasHeightForWidth())
        self.info_btn.setSizePolicy(sizePolicy)
        self.info_btn.setObjectName("info_btn")
        self.horizontalLayout_2.addWidget(self.info_btn)
        self.horizontalLayout.addWidget(self.mainFrame)

        self.retranslateUi(JobPane)
        QtCore.QMetaObject.connectSlotsByName(JobPane)

    def retranslateUi(self, JobPane):
        JobPane.setWindowTitle(QtWidgets.QApplication.translate("JobPane", "JobPane", None, -1))
        self.id_label.setText(QtWidgets.QApplication.translate("JobPane", "jobid", None, -1))
        self.owner_label.setText(QtWidgets.QApplication.translate("JobPane", "owner", None, -1))
        self.name_label.setText(QtWidgets.QApplication.translate("JobPane", "Job Name", None, -1))
        self.queue_label.setText(QtWidgets.QApplication.translate("JobPane", "queuename", None, -1))
        self.info_btn.setText(QtWidgets.QApplication.translate("JobPane", "Job Info", None, -1))

from DetailsPane import DetailsPane
from ElidedLabel import ElidedLabel
from . import main_rc

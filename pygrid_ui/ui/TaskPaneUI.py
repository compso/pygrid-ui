# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TaskPane.ui'
#
# Created: Fri Jul 14 12:10:18 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TaskPane(object):
    def setupUi(self, TaskPane):
        TaskPane.setObjectName("TaskPane")
        TaskPane.resize(483, 41)
        TaskPane.setFrameShape(QtWidgets.QFrame.StyledPanel)
        TaskPane.setFrameShadow(QtWidgets.QFrame.Raised)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TaskPane)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.id_label = QtWidgets.QLabel(TaskPane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id_label.sizePolicy().hasHeightForWidth())
        self.id_label.setSizePolicy(sizePolicy)
        self.id_label.setObjectName("id_label")
        self.horizontalLayout.addWidget(self.id_label)
        self.queue_label = ElidedLabel(TaskPane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.queue_label.sizePolicy().hasHeightForWidth())
        self.queue_label.setSizePolicy(sizePolicy)
        self.queue_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.queue_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.queue_label.setObjectName("queue_label")
        self.horizontalLayout.addWidget(self.queue_label)
        self.status_label = QtWidgets.QLabel(TaskPane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setText("")
        self.status_label.setPixmap(QtGui.QPixmap(":/res/png/warning.png"))
        self.status_label.setObjectName("status_label")
        self.horizontalLayout.addWidget(self.status_label)
        self.log_btn = QtWidgets.QPushButton(TaskPane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_btn.sizePolicy().hasHeightForWidth())
        self.log_btn.setSizePolicy(sizePolicy)
        self.log_btn.setObjectName("log_btn")
        self.horizontalLayout.addWidget(self.log_btn)

        self.retranslateUi(TaskPane)
        QtCore.QObject.connect(self.log_btn, QtCore.SIGNAL("clicked()"), TaskPane._view_logs)
        QtCore.QMetaObject.connectSlotsByName(TaskPane)

    def retranslateUi(self, TaskPane):
        TaskPane.setWindowTitle(QtWidgets.QApplication.translate("TaskPane", "Frame", None, -1))
        self.id_label.setText(QtWidgets.QApplication.translate("TaskPane", "taskid", None, -1))
        self.queue_label.setText(QtWidgets.QApplication.translate("TaskPane", "queue_name", None, -1))
        self.log_btn.setText(QtWidgets.QApplication.translate("TaskPane", "View Log", None, -1))

from ElidedLabel import ElidedLabel
from . import main_rc
from . import main_rc
from . import main_rc
from . import main_rc

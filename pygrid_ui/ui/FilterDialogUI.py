# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FilterDialog.ui'
#
# Created: Mon Jul 10 15:29:03 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FilterDialog(object):
    def setupUi(self, FilterDialog):
        FilterDialog.setObjectName("FilterDialog")
        FilterDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(FilterDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(FilterDialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.complex_filter_list = QtWidgets.QListWidget(self.splitter)
        self.complex_filter_list.setObjectName("complex_filter_list")
        self.complex_list = QtWidgets.QListWidget(self.splitter)
        self.complex_list.setObjectName("complex_list")
        self.horizontalLayout.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(FilterDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.owner_filter_label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.owner_filter_label.sizePolicy().hasHeightForWidth())
        self.owner_filter_label.setSizePolicy(sizePolicy)
        self.owner_filter_label.setObjectName("owner_filter_label")
        self.verticalLayout_2.addWidget(self.owner_filter_label)
        self.owner_filter_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.owner_filter_lineEdit.setClearButtonEnabled(False)
        self.owner_filter_lineEdit.setObjectName("owner_filter_lineEdit")
        self.verticalLayout_2.addWidget(self.owner_filter_lineEdit)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(FilterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(FilterDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), FilterDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), FilterDialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("clicked(QAbstractButton*)"), FilterDialog.on_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(FilterDialog)

    def retranslateUi(self, FilterDialog):
        FilterDialog.setWindowTitle(QtWidgets.QApplication.translate("FilterDialog", "Dialog", None, -1))
        self.owner_filter_label.setText(QtWidgets.QApplication.translate("FilterDialog", "Filter by owner (default blank = just you)", None, -1))
        self.owner_filter_lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("FilterDialog", "username, username, ...", None, -1))


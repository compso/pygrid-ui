# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Fri Jul  7 18:16:46 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.jobs_tab = QtWidgets.QWidget()
        self.jobs_tab.setObjectName("jobs_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.jobs_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.jobs_tab)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.running_scroll = QtWidgets.QScrollArea(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.running_scroll.sizePolicy().hasHeightForWidth())
        self.running_scroll.setSizePolicy(sizePolicy)
        self.running_scroll.setWidgetResizable(True)
        self.running_scroll.setObjectName("running_scroll")
        self.running_w = QtWidgets.QWidget()
        self.running_w.setGeometry(QtCore.QRect(0, 0, 659, 283))
        self.running_w.setObjectName("running_w")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.running_w)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.running_scroll.setWidget(self.running_w)
        self.pending_scroll = QtWidgets.QScrollArea(self.splitter)
        self.pending_scroll.setWidgetResizable(True)
        self.pending_scroll.setObjectName("pending_scroll")
        self.pending_w = QtWidgets.QWidget()
        self.pending_w.setGeometry(QtCore.QRect(0, 0, 659, 162))
        self.pending_w.setObjectName("pending_w")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pending_w)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pending_scroll.setWidget(self.pending_w)
        self.verticalLayout.addWidget(self.splitter)
        self.frame = QtWidgets.QFrame(self.jobs_tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.refresh_btn = QtWidgets.QPushButton(self.frame)
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout_3.addWidget(self.refresh_btn)
        self.verticalLayout.addWidget(self.frame)
        self.tabWidget.addTab(self.jobs_tab, "")
        self.hosts_tab = QtWidgets.QWidget()
        self.hosts_tab.setObjectName("hosts_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.hosts_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.hosts_tab)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.tabWidget.addTab(self.hosts_tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.delete_btn = QtWidgets.QPushButton(self.frame_2)
        self.delete_btn.setObjectName("delete_btn")
        self.verticalLayout_5.addWidget(self.delete_btn)
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4)
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_5.addWidget(self.line_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_5.addWidget(self.pushButton_7)
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_5.addWidget(self.line_3)
        self.filters_btn = QtWidgets.QPushButton(self.frame_2)
        self.filters_btn.setObjectName("filters_btn")
        self.verticalLayout_5.addWidget(self.filters_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuControl = QtWidgets.QMenu(self.menubar)
        self.menuControl.setObjectName("menuControl")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionRescedule = QtWidgets.QAction(MainWindow)
        self.actionRescedule.setObjectName("actionRescedule")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSuspend = QtWidgets.QAction(MainWindow)
        self.actionSuspend.setObjectName("actionSuspend")
        self.actionResume = QtWidgets.QAction(MainWindow)
        self.actionResume.setObjectName("actionResume")
        self.actionHold = QtWidgets.QAction(MainWindow)
        self.actionHold.setObjectName("actionHold")
        self.menuSettings.addAction(self.actionSettings)
        self.menuControl.addAction(self.actionRescedule)
        self.menuControl.addAction(self.actionDelete)
        self.menuControl.addAction(self.actionSuspend)
        self.menuControl.addAction(self.actionResume)
        self.menuControl.addAction(self.actionHold)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuControl.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "QStat Gui", None, -1))
        self.refresh_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Refresh", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.jobs_tab), QtWidgets.QApplication.translate("MainWindow", "Jobs", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "Hostname", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hosts_tab), QtWidgets.QApplication.translate("MainWindow", "Hosts", None, -1))
        self.delete_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Hold", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Suspend", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "Resume", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "Reschedule", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Clear error", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "Set Priority", None, -1))
        self.pushButton_7.setText(QtWidgets.QApplication.translate("MainWindow", "QAlter", None, -1))
        self.filters_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Filter", None, -1))
        self.menuSettings.setTitle(QtWidgets.QApplication.translate("MainWindow", "Main", None, -1))
        self.menuControl.setTitle(QtWidgets.QApplication.translate("MainWindow", "Control", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.actionSettings.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.actionRescedule.setText(QtWidgets.QApplication.translate("MainWindow", "Rescedule", None, -1))
        self.actionDelete.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.actionSuspend.setText(QtWidgets.QApplication.translate("MainWindow", "Suspend", None, -1))
        self.actionResume.setText(QtWidgets.QApplication.translate("MainWindow", "Resume", None, -1))
        self.actionHold.setText(QtWidgets.QApplication.translate("MainWindow", "Hold", None, -1))

from . import main_rc

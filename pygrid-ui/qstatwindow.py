
from PySide2 import QtWidgets, QtCore
from ui import Ui_MainWindow


class QStatWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        super(QStatWindow, self).__init__(parent, *args, **kwargs)

        self.mainwindow = Ui_MainWindow()
        self.mainwindow.setupUi(self)

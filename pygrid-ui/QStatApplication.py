
from PySide2 import QtWidgets, QtCore
from .ui import MainWindow


class QStatApplication(QtWidgets.QApplication):

    def __init__(self):
        super(QStatApplication, self).__init__()

    def setup(self):
        self.mainwindow = MainWindow()

    def run(self):
        self.mainwindow.show()
        return self.exec_()

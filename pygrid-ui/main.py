
import sys
from PySide2 import QtWidgets, QtCore
from qstatwindow import QStatWindow


def main(*args, **kwargs):

    app = QtWidgets.QApplication(*args, **kwargs)
    window = QStatWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main(sys.argv))

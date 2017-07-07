from PySide2 import QtWidgets
from LogDialogUI import Ui_LogDialog
import os


class LogDialog(QtWidgets.QDialog):

    def __init__(self, parent=None, log_file=''):
        super(LogDialog, self).__init__(parent)

        self.ui = Ui_LogDialog()
        self.ui.setupUi(self)

        self.log_file = log_file

        if os.path.isfile(log_file):
            log_f = open(log_file, "r")
            log_data = log_f.read()
            log_f.close()

            self.setText(log_data)
        else:
            print "Log file doesn't exist: {}".format(log_file)

    def setText(self, text):

        self.ui.textEdit.setText(text)

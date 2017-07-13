from PySide2 import QtWidgets, QtCore
from TaskPaneUI import Ui_TaskPane
from LogDialog import LogDialog
import os


class TaskPane(QtWidgets.QFrame):

    doubleClicked = QtCore.Signal()

    def __init__(self, parent=None):
        super(TaskPane, self).__init__(parent)

        self.job_info = {}
        self.task = {}

        self.ui = Ui_TaskPane()
        self.ui.setupUi(self)

        self.setObjectName('TaskPane')
        self.setStyleSheet("TaskPane {border: 1px solid rgb(125,125,125)}"
                           "TaskPane:hover {background: rgb(125,125,125)}")

        self.doubleClicked.connect(self._view_logs)

    def mouseDoubleClickEvent(self, event):
        super(TaskPane, self).mouseDoubleClickEvent(event)

        if event.button() is QtCore.Qt.LeftButton:
            self.doubleClicked.emit()

    def _view_logs(self):

        logs_path = self.job_info.get('out_log_paths', [])
        print logs_path

        if len(logs_path):
            this_log = logs_path[0].get('path')

            os.environ['JOB_ID'] = str(self.job_info['jobid'])
            os.environ['TASK_ID'] = str(self.task.get('tasks', 1))

            log_file = os.path.expandvars(this_log)

            if os.path.isdir(log_file):

                if self.task.get('tasks'):

                    log_file_name = '{}.o{}.{}'.format(self.job_info['name'],
                                                       self.job_info['jobid'],
                                                       self.task['tasks'])
                else:

                    log_file_name = '{}.o{}'.format(self.job_info['name'],
                                                    self.job_info['jobid'])

                log_file = os.path.join(log_file, log_file_name)

            if os.path.isfile(log_file):

                log_dialog = LogDialog(self, log_file)
                log_dialog.setWindowTitle('Task log ({}.{})'.format(self.job_info['jobid'],
                                                                    self.task.get('tasks', 1)))
                log_dialog.show()
            else:
                # popup no log error

                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Log Error")
                msgBox.setInformativeText("The log '{}' doesnot exist".format(log_file))
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                return msgBox.exec_()

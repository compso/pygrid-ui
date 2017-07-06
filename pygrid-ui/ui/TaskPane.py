from PySide2 import QtWidgets
from TaskPaneUI import Ui_TaskPane


class TaskPane(QtWidgets.QFrame):

    def __init__(self, parent=None):
        super(TaskPane, self).__init__(parent)

        self.ui = Ui_TaskPane()
        self.ui.setupUi(self)

        self.setObjectName('TaskPane')
        self.setStyleSheet("TaskPane {border: 1px solid rgb(125,125,125);}")

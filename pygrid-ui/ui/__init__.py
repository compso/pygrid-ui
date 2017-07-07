from Color import Color
from Style import Style
from JobInfoDialog import JobInfoDialog
from MainWindowUI import Ui_MainWindow
from JobPaneUI import Ui_JobPane
from ElidedLabel import ElidedLabel
from FiltersDialog import FiltersDialog

from PySide2 import QtWidgets


def clearWidget(widget):
    """clear children from given widget"""
    while widget.layout().count():
        item = widget.layout().takeAt(0)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QSpacerItem):
            widget.layout().removeItem(item)

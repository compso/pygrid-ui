
from PySide2 import QtCore, QtWidgets


class DetailsPane(QtWidgets.QFrame):

    selected = QtCore.Signal()
    deselected = QtCore.Signal()

    def __init__(self, parent=None):
        super(DetailsPane, self).__init__(parent)

        self.setObjectName('DetailsPane')
        self.setStyleSheet("DetailsPane {border: 1px solid rgb(125,125,125);}"
                           "DetailsPane:hover {background: rgb(125,125,125)}"
                           "DetailsPane[isSelected=true] {background: rgb(125, 125, 200)}")
        self.setMouseTracking(True)
        self.setProperty('isSelected', False)

    def isSelected(self):
        return self.property('isSelected')

    def setSelected(self, selected):
        self.setProperty('isSelected', selected)
        if self.isSelected():
            self.selected.emit()
        else:
            self.deselected.emit()
        self.setStyle(self.style())

    def mousePressEvent(self, event):
        super(DetailsPane, self).mousePressEvent(event)

        if event.button() == QtCore.Qt.LeftButton:

            isSelected = self.isSelected()
            self.setSelected(not isSelected)
            event.accept()

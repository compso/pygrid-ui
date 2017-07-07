from PySide2 import QtWidgets
from FilterDialogUI import Ui_FilterDialog


class FiltersDialog(QtWidgets.QDialog):

    def __init__(self, parent=None, filters={}):
        super(FiltersDialog, self).__init__(parent)

        self.filters = filters

        self.ui = Ui_FilterDialog()
        self.ui.setupUi(self)

        self._populate_filters()

    def _populate_filters(self):

        for f, v in self.filters.items():
            print f, v

    def get_filters(self):

        _filters = {}
        # names filter:
        names_text = self.ui.owner_filter_lineEdit.text()
        names = [n.strip() for n in names_text.split(',')]

        if len(names):
            _filters['user'] = names

        return _filters

    def on_button_clicked(self, button):

        ok_button = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
        save_button = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Save)

        if button in [ok_button, save_button]:
            self.filters = self.get_filters()


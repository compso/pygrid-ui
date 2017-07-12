
from PySide2 import QtWidgets, QtCore, QtGui
import api
from .ui import (Ui_MainWindow, JobPane, JobInfoDialog, FiltersDialog,
                 Style, clearWidget)

import sys
from copy import copy, deepcopy



class QStatWindow(QtWidgets.QMainWindow):

    refresh_jobs = QtCore.Signal(bool)

    def __init__(self, parent=None, style=None, *args, **kwargs):
        super(QStatWindow, self).__init__(parent, *args, **kwargs)
        
        if not style:
            style = Style.currentStyle()
        
        self.style = style
        self._panes = []
        self._selection = []
        # self._filters = {'user': '*'}
        self._filters = {}

        self._timer = QtCore.QTimer()

        self.applyStyle()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._setup_gui()

        self._pending_pane = self.ui.pending_w
        self._running_pane = self.ui.running_w

        # hide WIP buttone

        self._make_connections()

        self.list_jobs()

    def _setup_gui(self):

        for btn in ['suspend_btn', 'resume_btn',
                    'qalter_btn', 'hold_btn']:

            btn_w = getattr(self.ui, btn)
            btn_w.hide()

        self.ui.menubar.hide()

    def refresh_list(self, tabid):

        if tabid == 0:
            self.list_jobs()
        elif tabid == 1:
            self.list_hosts()

    def applyStyle(self):
        self.style.apply(self)
        
    def jobs():
        doc = "get and set the jobs list, refresh the view if set"

        def fget(self):
            return self.__jobs

        def fset(self, value):
            self.__jobs = value
            self.populate_jobs_list()

        return locals()

    jobs = property(**jobs())

    def hosts():
        doc = "get and set the hosts list, refresh the view if set"

        def fget(self):
            return self.__hosts

        def fset(self, value):
            self.__hosts = value
            self.populate_hosts_list()

        return locals()

    hosts = property(**hosts())

    def list_jobs(self):

        # set cursor to working
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        self.jobs = api.qstat.get_jobs(self._filters.items())
        
        QtWidgets.QApplication.restoreOverrideCursor()

    def add_job_pane(self, job):

        job_widget = JobPane(self, job=job)

        # job_widget.ui.info_btn.clicked.connect(lambda j=job: self.show_job_info(j))
        job_widget.selected.connect(lambda w=job_widget: self.add_selection(w))
        job_widget.deselected.connect(lambda w=job_widget: self.remove_selection(w))

        if job_widget.isrunning():
            self._running_pane.layout().addWidget(job_widget)
        else:
            self._pending_pane.layout().addWidget(job_widget)

        if self.job_list_contains(job, self._selection):
            job_widget.setSelected(True, False)

        self._panes.append(job_widget)

    def add_selection(self, pane):

        # get if the Ctrl key is down
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if modifiers == QtCore.Qt.ShiftModifier:
            # get the panes between this one that next selected one
            start = False
            for p in self._panes:
                if not start and p == pane and not p.isSelected():
                    start = True
                    p.setSelected(True)
                elif start and not p.isSelected():
                    p.setSelected(True)
                    self._selection.append(copy(p.job))
                elif start and p.isSelected():
                    break
                elif start and p == pane:
                    break
                elif not start and p.isSelected():
                    start = True

        elif modifiers == QtCore.Qt.ControlModifier:
            pass
        else:
            for j in self._selection:
                p = self.get_job_pane(j)
                if p:
                    p.setSelected(False)

        if pane.job not in self._selection:
            self._selection.append(copy(pane.job))

    def get_job_pane(self, job):
        for p in self._panes:
            if p.job == job:
                return p
        return None

    def remove_selection(self, pane):

        if pane.job in self._selection:
            idx = self._selection.index(pane.job)
            self._selection.pop(idx)

    def job_list_contains(self, job, joblist):
        return job['jobid'] in [j['jobid'] for j in joblist]

    def populate_jobs_list(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        clearWidget(self._pending_pane)
        clearWidget(self._running_pane)

        self._panes = []
        # refresh the selection list, if any jobs are removed
        self._selection = [j for j in self._selection if self.job_list_contains(j, self.jobs)]
        print [j['jobid'] for j in self._selection]

        for j in sorted(self.jobs, key=lambda k: k['jobid']):
            self.add_job_pane(j)

        # add spacer to the bottom of both the panes

        self.__add_spacer(self._pending_pane)
        self.__add_spacer(self._running_pane)
        
        QtWidgets.QApplication.restoreOverrideCursor()

    def list_hosts(self):

        self.hosts = api.qhost.get_hosts(True)

    def populate_hosts_list(self):

        self.ui.hosts_tree.clear()

        for h in sorted(self.hosts, key=lambda k: k['hostname']):
            this_hosts_item = QtWidgets.QTreeWidgetItem()
            this_hosts_item.setText(0, h.get('hostname'))
            if len(h.get('jobs', [])):
                for j in h['jobs']:
                    j_item = QtWidgets.QTreeWidgetItem(this_hosts_item)
                    j_item.setText(0, j.get('job_name'))

            self.ui.hosts_tree.addTopLevelItem(this_hosts_item)

    def __add_spacer(self, widget):

        widget.layout().addSpacerItem(
            QtWidgets.QSpacerItem(1, 1,
                                  QtWidgets.QSizePolicy.Expanding,
                                  QtWidgets.QSizePolicy.Expanding))

    def show_job_info(self, job):

        job_info = api.qstat.get_job_info(job['jobid'])[-1]

        # job_info['tasks'] = filter(lambda d: d['jobid'] == job['jobid'], self.jobs)

        job_dialog = JobInfoDialog(self, job_info)
        job_dialog.setWindowTitle('Job Info ({})'.format(job['jobid']))

        job_dialog.exec_()

    def run_filter_dialog(self):

        self.filter_dialog = FiltersDialog(self, self._filters)
        self.filter_dialog.accepted.connect(self.set_filters)

        self.filter_dialog.show()

    def set_filters(self):

        self._filters = self.filter_dialog.filters

        self.list_jobs()

    def delete_jobs(self):

        ids = []

        for j in self._selection:
            n = j.id_label.text()
            # if j['tasks'].isdigit():
            #     n = '{}.{}'.format(n, j['tasks'])
            ids.append(n)

        confirm = self.__confirm_message(
            "Are you sure you want to delete these jobs?",
            "this can not be undone", QtWidgets.QMessageBox.Cancel)

        if confirm == QtWidgets.QMessageBox.Ok:
            api.qdel.delete_jobs(ids)
            self.list_jobs()

    def clear_error(self):

        ids = []

        for j in self._selection:
            n = j.id_label.text()
            # if j['tasks'].isdigit():
            #     n = '{}.{}'.format(n, j['tasks'])
            ids.append(str(n))

        api.qmod.clear_error(ids)
        self.list_jobs()

    def reschedule_jobs(self):

        ids = []

        for j in self._selection:
            n = j.get('jobid')
            # if j['tasks'].isdigit():
            #     n = '{}.{}'.format(n, j['tasks'])
            ids.append(str(n))

        api.qmod.rescedule_jobs(ids)
        self.list_jobs()

    def set_auto_refresh(self, refresh=False):
        if refresh:
            self._timer.setInterval(5000)
            self._timer.start()
        else:
            self._timer.stop()

    def set_priority(self):

        cur_priority = 0
        num_selected = len(self._selection)
        if num_selected == 1:
            cur_priority = self._selection[0].get('priority', 0)
        priority, result = QtWidgets.QInputDialog.getInt(self,
                                                         "Set User Priority",
                                                         "Priority",
                                                         cur_priority, -1024, 1024)
        if result and num_selected:
            api.qalter.set_priority(priority, [j['jobid'] for j in self._selection])

    def __confirm_message(self, text, info_text, default=QtWidgets.QMessageBox.Ok):

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setInformativeText(info_text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msgBox.setDefaultButton(default)
        return msgBox.exec_()

    def _make_connections(self):

        self.ui.refresh_btn.clicked.connect(self.list_jobs)
        self.ui.filters_btn.clicked.connect(self.run_filter_dialog)

        self._timer.timeout.connect(self.list_jobs)


def main(*args, **kwargs):

    app = QtWidgets.QApplication(sys.argv)
    window = QStatWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main(sys.argv))

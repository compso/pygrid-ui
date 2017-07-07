
from PySide2 import QtWidgets, QtCore, QtGui
from ui import (Ui_MainWindow, Ui_JobPane, JobInfoDialog, FiltersDialog,
                Style, clearWidget)
import api

STATUS_ICONS = {'r': ':/res/png/running.png',
                'qw': ':/res/png/waiting.png',
                'hqw': ':/res/png/onhold.png',
                'Eqw': ':/res/png/error.png'}


def get_status_icon(status):
    icon = ":/res/png/waiting.png"

    if status in STATUS_ICONS:
        icon = STATUS_ICONS[status]

    return icon


class QStatWindow(QtWidgets.QMainWindow):

    refresh_jobs = QtCore.Signal(bool)

    def __init__(self, parent=None, style=None, *args, **kwargs):
        super(QStatWindow, self).__init__(parent, *args, **kwargs)
        
        if not style:
            style = Style.currentStyle()
        
        self.style = style
        self._panes = []
        self._selection = []
        self._filters = {}

        self.applyStyle()
        self.mainwindow = Ui_MainWindow()
        self.mainwindow.setupUi(self)

        self._pending_pane = self.mainwindow.pending_w
        self._running_pane = self.mainwindow.running_w

        self._make_connections()

        self.list_jobs()

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

    def list_jobs(self):

        self.jobs = api.qstat.get_jobs(self._filters.items())

    def add_job_pane(self, job):

        job_status = job.get('flags', 'qw')

        job_widget = QtWidgets.QWidget()
        job_widget.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                                       QtWidgets.QSizePolicy.Maximum))
        this_pane = Ui_JobPane()
        this_pane.setupUi(job_widget)
        status_icon = get_status_icon(job_status)

        this_pane.status_label.setPixmap(QtGui.QPixmap(status_icon))

        jobid = str(job.get('jobid', '0'))

        if 'tasks' in job and job_status == 'r':
            jobid = '{}.{}'.format(jobid, job['tasks'])

        this_pane.id_label.setText(jobid)
        this_pane.owner_label.setText(job.get('owner', 'none'))
        this_pane.name_label.setText(job.get('name', 'none'))

        this_pane.info_btn.clicked.connect(lambda j=job: self.show_job_info(j))
        this_pane.mainFrame.selected.connect(lambda w=this_pane: self.add_selection(w))
        this_pane.mainFrame.deselected.connect(lambda w=this_pane: self.remove_selection(w))

        if job_status == 'r':
            this_pane.queue_label.setText(job.get('running_queue', 'u.q'))
            self._running_pane.layout().insertWidget(0, job_widget)
        else:
            this_pane.queue_label.setText(job.get('requested_queue', 'r.q'))
            self._pending_pane.layout().insertWidget(0, job_widget)

        self._panes.append(this_pane)

    def add_selection(self, pane):

        # get if the Ctrl key is down
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if modifiers == QtCore.Qt.ShiftModifier:
            # get the panes between this one that next selected one
            start = False
            for p in self._panes:
                if not start and p == pane and not p.mainFrame.isSelected():
                    start = True
                    p.mainFrame.setSelected(True)
                elif start and not p.mainFrame.isSelected():
                    p.mainFrame.setSelected(True)
                    self._selection.append(p)
                elif start and p.mainFrame.isSelected():
                    break
                elif start and p == pane:
                    break
                elif not start and p.mainFrame.isSelected():
                    start = True

        elif modifiers == QtCore.Qt.ControlModifier:
            pass
        else:
            for p in self._selection:
                p.mainFrame.setSelected(False)

        if pane not in self._selection:
            self._selection.append(pane)

    def remove_selection(self, pane):

        if pane in self._selection:
            idx = self._selection.index(pane)
            self._selection.pop(idx)

    def populate_jobs_list(self):

        clearWidget(self._pending_pane)
        clearWidget(self._running_pane)

        self._panes = []
        self._selection = []

        for j in self.jobs:
            self.add_job_pane(j)

        # add spacer to the bottom of both the panes

        self.__add_spacer(self._pending_pane)
        self.__add_spacer(self._running_pane)

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

        job_dialog.show()

    def run_filter_dialog(self):

        self.filter_dialog = FiltersDialog(self, self._filters)

        self.filter_dialog.show()

        self.filter_dialog.accepted.connect(self.set_filters)

    def set_filters(self):

        self._filters = self.filter_dialog.filters

        self.list_jobs()

    def delete_jobs(self):

        ids = []

        for j in self._selection:
            n = j.get('jobid')
            if j['tasks'].isdigit():
                n = '{}.{}'.format(n, j['tasks'])
            ids.append(n)

        confirm = self.__confirm_message(
            "Are you sure you want to delete these jobs?",
            "this can not be undone", QtWidgets.QMessageBox.Cancel)

        if confirm == QtWidgets.QMessageBox.Ok:
            api.qdel.delete_jobs(ids)

    def __confirm_message(self, text, info_text, default=QtWidgets.QMessageBox.Ok):

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setInformativeText(info_text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msgBox.setDefaultButton(default)
        return msgBox.exec_()

    def _make_connections(self):

        self.mainwindow.refresh_btn.clicked.connect(self.list_jobs)
        self.mainwindow.filters_btn.clicked.connect(self.run_filter_dialog)


from PySide2 import QtCore, QtWidgets, QtGui
from .JobPaneUI import Ui_JobPane
from . import JobInfoDialog
from ..api import qstat

from copy import deepcopy


STATUS_ICONS = {'r': ':/res/png/running.png',
                'qw': ':/res/png/waiting.png',
                'hqw': ':/res/png/onhold.png',
                'Eqw': ':/res/png/error.png'}


def get_status_icon(status):
    icon = ":/res/png/waiting.png"

    if status in STATUS_ICONS:
        icon = STATUS_ICONS[status]

    return icon


class JobPane(QtWidgets.QFrame):

    selected = QtCore.Signal()
    deselected = QtCore.Signal()
    doubleClicked = QtCore.Signal()

    def __init__(self, parent=None, job={}):
        super(JobPane, self).__init__(parent)

        self.job = deepcopy(job)

        self.ui = Ui_JobPane()
        self.ui.setupUi(self)

        self.setObjectName('JobPane')
        self.setStyleSheet("JobPane {border: 1px solid rgb(125,125,125);}"
                           "JobPane:hover {background: rgb(125,125,125)}"
                           "JobPane[isSelected=true] {background: rgb(125, 125, 200)}")
        self.setMouseTracking(True)
        self.setProperty('isSelected', False)
        # self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
        #                                          QtWidgets.QSizePolicy.Preferred))

        self.setup_job()

        self.doubleClicked.connect(self.show_job_info)

    def setup_job(self):

        job_status = self.job.get('flags', 'qw')

        status_icon = get_status_icon(job_status)

        self.ui.status_label.setPixmap(QtGui.QPixmap(status_icon))

        jobid = str(self.job.get('jobid', '0'))

        if 'tasks' in self.job and self.job['tasks'].isdigit():
            jobid = '{}.{}'.format(jobid, self.job['tasks'])

        self.ui.id_label.setText(jobid)
        self.ui.owner_label.setText(self.job.get('owner', 'none'))
        self.ui.name_label.setText(self.job.get('name', 'none'))
        if self.job.get('submission_time'):
            self.ui.spool_label.setText(self.job.get('submission_time'))
        elif self.job.get('start_time'):
            self.ui.spool_label.setText(self.job.get('start_time'))

        if self.isrunning():
            self.ui.queue_label.setText(self.job.get('running_queue', 'u.q'))
        else:
            self.ui.queue_label.setText(','.join(self.job.get('requested_queue', 'r.q')))

    def isrunning(self):
        return self.job.get('flags') in ['r', 't']

    def isSelected(self):
        return self.property('isSelected')

    def setSelected(self, selected, emit=True):
        self.setProperty('isSelected', selected)
        if emit:
            if self.isSelected():
                self.selected.emit()
            else:
                self.deselected.emit()
        self.setStyle(self.style())

    def mousePressEvent(self, event):
        super(JobPane, self).mousePressEvent(event)

        if event.button() == QtCore.Qt.LeftButton:

            isSelected = self.isSelected()
            self.setSelected(not isSelected)
            event.accept()

    def mouseDoubleClickEvent(self, event):
        super(JobPane, self).mouseDoubleClickEvent(event)

        if event.button() is QtCore.Qt.LeftButton:
            self.doubleClicked.emit()

    def show_job_info(self):

        jobid = self.job.get('jobid')

        try:
            job_info = qstat.get_job_info(jobid)
            if len(job_info):
                job_info = job_info[-1]
            job_dialog = JobInfoDialog(self.parentWidget(), job_info)
            job_dialog.setWindowTitle('Job Info ({})'.format(jobid))

            job_dialog.show()
        except Exception:
            raise

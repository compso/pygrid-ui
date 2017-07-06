
from PySide2 import QtWidgets, QtGui
from JobInfoDialogUI import Ui_JobInfoDialog
from TaskPane import TaskPane

import re

STATUS_ICONS = {'r': ':/res/png/running.png',
                't': ':/res/png/running.png',
                'qw': ':/res/png/waiting.png',
                'hqw': ':/res/png/onhold.png',
                'Eqw': ':/res/png/error.png'}


def get_status_icon(status):
    icon = ":/res/png/waiting.png"

    if status in STATUS_ICONS:
        icon = STATUS_ICONS[status]

    return icon


class JobInfoDialog(QtWidgets.QDialog):

    def __init__(self, parent=None, job_info={}):
        super(JobInfoDialog, self).__init__(parent)

        self.job_info = job_info

        self.ui = Ui_JobInfoDialog()
        self.ui.setupUi(self)

        self._populate_tasks()

    def _get_pending_tasks(self, tasks):

        out_task_ids = []

        pending_tasks = filter(lambda d: d['state'] == 'pending', tasks)
        if len(pending_tasks):
            taskid_str = pending_tasks[0].get('tasks')
            task_ranges = taskid_str.split(',')
            for tr in task_ranges:
                tr_m = re.match(r'(\d+)-(\d+):(\d+)', tr)


        return out_task_ids

    def _populate_tasks(self):

        s = self.job_info.get('task_range')
        tasks = self.job_info.get('tasks')[0]
        pending_tasks = filter(lambda d: d['state'] == 'pending', tasks)
        print pending_tasks[0]['tasks']
        for i in range(s['min'], s['max'] + 1, s['step']):
            _t = TaskPane(self)
            _t.ui.id_label.setText(str(i))
            status = 'w'
            this_task = filter(lambda d: d['tasks'] == str(i), tasks)
            if len(this_task):
                print this_task
                _t.task = this_task[0]
                status = this_task[0]['flags']

                if status == 'r':
                    _t.ui.queue_label.setText(this_task[0].get('running_queue', 'u.q'))
                else:
                    _t.ui.queue_label.hide()
            
            status_icon = get_status_icon(status)

            _t.ui.status_label.setPixmap(QtGui.QPixmap(status_icon))

            self.ui.taskInfo_w.layout().addWidget(_t)

        self.ui.taskInfo_w.layout().addSpacerItem(
            QtWidgets.QSpacerItem(1, 1,
                                  QtWidgets.QSizePolicy.Expanding,
                                  QtWidgets.QSizePolicy.Expanding))

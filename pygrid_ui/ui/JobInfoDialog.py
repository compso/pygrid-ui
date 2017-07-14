
from PySide2 import QtWidgets, QtGui
from JobInfoDialogUI import Ui_JobInfoDialog
from .TaskPane import TaskPane
import re
from copy import deepcopy
from ..api import qstat


STATUS_ICONS = {'r': ':/res/png/running.png',
                'Rr': ':/res/png/running.png',
                't': ':/res/png/running.png',
                'qw': ':/res/png/waiting.png',
                'hqw': ':/res/png/onhold.png',
                'f': ':/res/png/finished.png',
                'Eqw': ':/res/png/error.png'}


def get_status_icon(status):
    icon = ":/res/png/waiting.png"

    if status in STATUS_ICONS:
        icon = STATUS_ICONS[status]

    return icon


class JobInfoDialog(QtWidgets.QDialog):

    def __init__(self, parent=None, job_info={}):
        super(JobInfoDialog, self).__init__(parent)

        self.job_info = deepcopy(job_info)
        self.tasks = []

        self.ui = Ui_JobInfoDialog()
        self.ui.setupUi(self)

        self.get_tasks()

        self._populate_tasks()
        self._populate_info()

    def get_tasks(self):

        all_jobs = qstat.get_jobs([('user', self.job_info['owner'])])
        self.tasks = filter(lambda x: x['jobid'] == self.job_info['jobid'], all_jobs)

    def _get_pending_tasks(self, tasks):

        out_task_ids = []

        if len(tasks):
            taskid_str = tasks[0].get('tasks')
            if taskid_str:
                task_ranges = taskid_str.split(',')
                for tr in task_ranges:
                    tr_m = re.match(r'(\d+)-(\d+):(\d+)|(\d+)', tr)
                    if tr_m:
                        s, e, st, tid = tr_m.groups()
                        if tid:
                            out_task_ids.append(tid)
                        else:
                            out_task_ids += [str(i) for i in range(int(s), int(e) + 1, int(st))]

        return out_task_ids

    def _populate_tasks(self):

        s = self.job_info.get('task_range')
        pending_tasks = filter(lambda d: d['state'] == 'pending', self.tasks)
        pending_tids = self._get_pending_tasks(pending_tasks)
        for i in range(s['min'], s['max'] + 1, s['step']):
            _t = TaskPane(self)
            _t.ui.id_label.setText(str(i))
            _t.job_info = self.job_info
            status = 'w'

            this_task = filter(lambda d: d.get('tasks', 'n') == str(i), self.tasks)
            if len(this_task):
                _t.task = this_task[0]
                status = this_task[0]['flags']
                if status in ['r', 't', 'Rr']:
                    _t.ui.queue_label.setText(this_task[0].get('running_queue', 'all.q'))
                else:
                    _t.ui.queue_label.hide()
            elif str(i) in pending_tids:
                # set status to the same as the host job
                _t.task = pending_tasks[0].copy()
                _t.task['tasks'] = str(i)
                status = _t.task.get('flags')
                _t.ui.queue_label.setText(','.join(_t.task.get('requested_queue', 'r.q')))
            elif s['min'] == s['max']:
                # set status to the same as the host job
                # _t.task['tasks'] = str(i)
                if len(pending_tasks):
                    status = pending_tasks[0].get('flags')
                    print _t.job_info
                    _t.ui.queue_label.setText(_t.job_info.get('running_queue', 'u.q'))
                else:
                    status = 'r'
            else:
                # job is finished
                _t.task['tasks'] = str(i)
                status = 'f'
            
            status_icon = get_status_icon(status)

            _t.ui.status_label.setPixmap(QtGui.QPixmap(status_icon))

            self.ui.taskInfo_w.layout().addWidget(_t)

        self.ui.taskInfo_w.layout().addSpacerItem(
            QtWidgets.QSpacerItem(1, 1,
                                  QtWidgets.QSizePolicy.Expanding,
                                  QtWidgets.QSizePolicy.Expanding))

    def _populate_info(self):

        r = 0
        for k, v in self.job_info.items():

            if k in ['successors', 'predecessors']:
                v = ','.join([str(p['id']) for p in v])
            elif k in ['out_log_paths', 'shell']:
                v = ','.join([p['path'] for p in v])
            elif k == 'pe_range':
                v = '{}-{}:{}'.format(v['min'], v['max'], v['step'])
            elif k in ['requested_queues']:
                v = ','.join([q['name'] for q in v])

            key_item = QtWidgets.QTableWidgetItem("{}".format(k))
            value_item = QtWidgets.QTableWidgetItem("{}".format(v))
            self.ui.details_table.insertRow(r)
            self.ui.details_table.setItem(r, 0, key_item)
            self.ui.details_table.setItem(r, 1, value_item)

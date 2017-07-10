
from pygrid import QAcctCommand


def get_job_finished_tasks(jobid):

    qacct = QAcctCommand()
    return qacct.get_finished_tasks(jobid)

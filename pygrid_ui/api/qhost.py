
from pygrid import QHostCommand


def get_hosts(show_jobs=False):
    """
    filters list of 2 part tuples

        [('user', '*')]
        [('user', ['username', 'username2'])]

        if no filters are give qstat defaults to just showing your own jobs
    """

    qhost = QHostCommand()
    hosts = qhost.listHosts(show_jobs)

    return hosts

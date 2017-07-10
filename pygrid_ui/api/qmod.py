
from pygrid import QModCommand


def clear_error(obj_list):
    """
    filters list of 2 part tuples

        [('user', '*')]
        [('user', ['username', 'username2'])]

        if no filters are give qstat defaults to just showing your own jobs
    """

    qmod = QModCommand()
    result = qmod.clear_error(obj_list)

    return result


from pygrid import QAlterCommand


def set_priority(priority, obj_list, force=False):
    """
    priority: int
    obj_lsist: list of jobids
    """

    qalter = QAlterCommand()
    result = qalter.set_priority(priority, obj_list, force)

    return result

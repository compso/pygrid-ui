

from pygrid import QDelCommand


def delete_jobs(ids, force=False):
    """
    ids list job ids to delete
    """

    qdel = QDelCommand()
    output = qdel.delete_jobs(ids, force)

    return output

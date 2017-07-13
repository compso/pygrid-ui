from pygrid import QStatCommand


def get_jobs(filters=[]):
    """
    filters list of 2 part tuples

        [('user', '*')]
        [('user', ['username', 'username2'])]

        if no filters are give qstat defaults to just showing your own jobs
    """

    qstat = QStatCommand()
    args = []
    for f in filters:
        if f[0] == 'user':
            args.append('-u')
            if not isinstance(f[1], list):
                args.append(f[1])
            else:
                args += f[1]

    jobs = qstat.listJobs(args)

    return jobs


def get_job_info(jobid):
    """
    jobid int the id of the job you wan to get info about
    """

    qstat = QStatCommand()

    job_info = qstat.getJobInfo(jobid)

    return job_info

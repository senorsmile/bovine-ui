def load_jobs(requested_num=10):
    '''
    Input: num 
        - number of most recent jobs to return
        - defaults to 10

    Output: a dict of the last "num" of jobs
    '''




    #---------------------------------------
    # test_jobs: a temp var to pass back sample data
    #---------------------------------------
    test_jobs = {
        'jobs': {
            1: { 'nodes': 'web', 'job_length': '2:12', 'started': '2017/05/27 14:00:00', 'finished': '2017/05/27 13:02:12', 
                'job_percent': '100', 'summary': {"ok": 37, "changed": 1, "unreachable": 0, "failed": 0} },
            2: { 'nodes': 'web', 'job_length': '2:12', 'started': '2017/05/27 14:00:00', 'finished': '2017/05/27 13:02:12', 
                'job_percent': '100', 'summary': {"ok": 37, "changed": 1, "unreachable": 0, "failed": 0} },
            3: { 'nodes': 'web', 'job_length': '2:12', 'started': '2017/05/27 14:00:00', 'finished': '2017/05/27 13:02:12', 
                'job_percent': '100', 'summary': {"ok": 37, "changed": 1, "unreachable": 0, "failed": 0} },
            4: { 'nodes': 'web', 'job_length': '2:12', 'started': '2017/05/27 14:00:00', 'finished': '2017/05/27 13:02:12', 
                'job_percent': '100', 'summary': {"ok": 37, "changed": 1, "unreachable": 0, "failed": 0} },
            5: { 'nodes': 'web', 'job_length': '2:01', 'started': '2017/05/27 14:00:00', 'finished': '...',                 
                'job_percent': '99',  'summary': {"ok": 36, "changed": 0, "unreachable": 0, "failed": 0} },
            6: { 'nodes': 'db', 'job_length': '1:50', 'started': '2017/05/27 14:00:00', 'finished': '...',                 
                'job_percent': '59',  'summary': {"ok": 35, "changed": 5, "unreachable": 0, "failed": 0} },
        },
    }

    #---------------------------------------
    # determine the last job num 
    # i.e. convert all keys to ints, and get the max
    #---------------------------------------
    last_job_num= max(
        map(
            int, test_jobs['jobs']
        )
    )




    #---------------------------------------
    # calculate the range of jobs to return
    # starting at the last job, and counting backwards 
    # the requested_num of times
    #---------------------------------------
    num_range = []
    for i in range(last_job_num, last_job_num - requested_num, -1):
        num_range.append(i)



    jobs_limited = {'jobs': {}}
    for i in num_range:
        jobs_limited['jobs'][i] = test_jobs['jobs'][i]
    #---------------------------------------
    # return dict with data
    #---------------------------------------
    return {
        'deleteme': {
            'num_passed_to_func': requested_num,
            'num_range': num_range,
        },
        #'jobs': test_jobs['jobs'],
        'jobs': jobs_limited['jobs'],
        'last_job_num': last_job_num,
    }

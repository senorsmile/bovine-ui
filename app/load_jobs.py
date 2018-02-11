from flask import request
import os
import json

import mmap # for load_json_first_last
import linecache # for load_json_first_last

#def load_json_multiple(segments):
#    '''
#    INPUTS: 
#        segments -> a file obj
#    OUTPUTS:
#        generator giving one dict parsed from json
#    '''
#
#    chunk = ""
#    for segment in segments:
#        chunk += segment
#        try:
#            yield json.loads(chunk)
#            chunk = ""
#        except ValueError:
#            pass

def load_json_from_file(full_file_path):

    '''
    PURPOSE:
        - Load all lines of json from file,
        - parse the data as native python objects (i.e. dicts),
        - and return a list containing all the data, one parsed
          json object line per list item. 
    INPUTS:
        full_file_path -> str
            contains filename and path to load json from
    OUTPUTS:
        data -> list of dicts
            contains parsed data, one dict per list item
    '''
    
    f = open(full_file_path,'r')
    data = []
    for line in f:
        data.append(json.loads(line))

    return data[:]

def load_json_first_last(full_file_path):
    '''
    PURPOSE:
        - Load first and last lines of json from file,
        - parse the data
        - return in a list
    INPUTS:
    OUTPUTS:
    '''

    #--------------
    # first line
    #--------------
    first_line_raw = linecache.getline(full_file_path, 1)
    first_line = json.loads(first_line_raw)

    #--------------
    # last line
    #--------------
    with open(full_file_path, 'r') as source:
        mapping = mmap.mmap(source.fileno(), 0, prot=mmap.PROT_READ)

    last_line = json.loads(
        mapping[
            # mmap.rfind(string[, start[, end]])
            mapping.rfind(b'\n', 0, -1)+1:
        ]
    )

    #--------------
    # return
    #--------------
    return [
      first_line, 
      last_line,
    ]

def load_jobs(
    start_job_num,
    end_job_num,
    get_num_jobs,
):
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
    # check if there are real jobs on this node to display
    #---------------------------------------
    log_file_path='/.ansible/bovine/'
    log_file_path = os.path.expanduser('~') + log_file_path

    print("****** DEBUG: get_num_jobs? = " + str(get_num_jobs))

    if os.path.exists(log_file_path):
        filenames = sorted(list(os.walk(log_file_path))[0][2])

        test_jobs = {'jobs': {} }

        # parse data into test_jobs var
        job_num = 0
        for filename in filenames:
            job_num = job_num +1
            print("****** DEBUG: job_num = " + str(job_num))
            print("****** DEBUG: filename = " + str(filename))

            # skip ignored files
            if '.swp' in filename:
                job_num = job_num - 1
                continue

        last_job_num = job_num
        if get_num_jobs:
            return {
                'num_jobs': str(last_job_num),
                'start_job_num': str(start_job_num),
                'end_job_num': str(end_job_num),
            }

        job_num = 0
        for filename in filenames:
            job_num = job_num +1
            print("****** DEBUG: job_num = " + str(job_num))
            print("****** DEBUG: filename = " + str(filename))

            # skip ignored files
            if '.swp' in filename:
                job_num = job_num - 1
                continue

            # init this file's vars
            nodes_limit       = ''
            percent_completed = 0
            start_time        = ''
            end_time          = ''
            job_length        = ''
            ok                = 0
            changed           = 0
            unreachable       = 0
            failed            = 0


            # load & parse all lines from file
            # NB: file MUST have one valid json per line
            full_file_path = log_file_path + filename
            #filedata = load_json_from_file(full_file_path)
            filedata = load_json_first_last(full_file_path)

            for parsed_json in filedata:
                if   parsed_json["type"] == 'ANSIBLE START':
                    start_time = parsed_json["contents"]["start_time"]
                elif parsed_json["type"] == 'PLAY START':
                    pass
                elif parsed_json["type"] == 'NODE UNREACHABLE':
                    pass
                elif parsed_json["type"] == 'TASK START':
                    pass
                elif parsed_json["type"] == 'TASK OK':
                    pass
                elif parsed_json["type"] == 'TASK ITEM OK':
                    pass
                elif parsed_json["type"] == 'TASK FAILED':
                    pass
                elif parsed_json["type"] == 'TASK ITEM SKIPPED':
                    pass
                elif parsed_json["type"] == 'TASK ITEM FAILED':
                    pass
                elif parsed_json["type"] == 'TASK ITEM - HOST UNREACHABLE':
                    pass
                elif parsed_json["type"] == 'ALL PLAYS DONE':
                    #print("****** DEBUG: parsed_json = ")
                    #print(parsed_json)
                    percent_completed = 100
                    end_time = parsed_json["contents"]["end_time"]
                    job_length = parsed_json["contents"]["job_length"]

                    nodes_limit = "<br>".join(list(parsed_json["contents"]["stats"].keys()))
                    #ok = parsed_json["contents"]["stats"]
                    #changed =
                    #unreachable = 
                    #failed =
                else:
                    print("****** DEBUG: " + str(parsed_json["type"]) + ' parsed_json type not recognized')

            #print("****** DEBUG: job_num = " + str(job_num))
            test_jobs["jobs"][job_num] = {
                'nodes':        str(nodes_limit),
                'job_length':   str(job_length), 
                'started':      str(start_time), 
                'finished':     str(end_time), 
                'job_percent':  str(percent_completed),
                'summary': {
                    "ok":           ok, 
                    "changed":      changed, 
                    "unreachable":  unreachable, 
                    "failed":       failed,
                },
            }

            ##print("****** DEBUG: test_jobs = ")
            ##print(json.dumps(test_jobs,indent=4))

            #-----------------------
            # end of file loop
            #-----------------------
            

    #---------------------------------------
    # determine the last job num 
    # i.e. convert all keys to ints, and get the max
    #---------------------------------------
    #last_job_num = len(test_jobs + 1)
#    last_job_num= max(
#        map(
#            int, test_jobs['jobs']
#        )
#    )
    #print('****** DEBUG: last_job_num = ' + str(last_job_num))



    #---------------------------------------
    # calculate the range of jobs to return
    # starting at the last job, and counting backwards 
    # the end_job_num of times (or until we reach 1)
    #---------------------------------------
#    num_range = []
#    for i in range(last_job_num, last_job_num - end_job_num, -1):
#        if i > 0:
#            num_range.append(i)
#
#    #print("****** DEBUG: num_range = " + str(num_range)) # deleteme
#
#    jobs_limited = {'jobs': {}}
#    for i in num_range:
#        jobs_limited['jobs'][i] = test_jobs['jobs'][i]


    jobs_limited = {'jobs': {}}
    print("****** DEBUG: last_job_num = " + str(last_job_num)) # deleteme
    print("****** DEBUG: start_job_num = " + str(start_job_num)) # deleteme
    print("****** DEBUG: end_job_num = " + str(end_job_num)) # deleteme
    if start_job_num <= last_job_num:
        for i in range(end_job_num, start_job_num - 1, -1):
            jobs_limited['jobs'][i] = test_jobs['jobs'][i]
    else:
        jobs_limited['jobs'][start_job_num] = {}

    #print( # deleteme
    #  json.dumps(
    #      {
    #        'jobs': jobs_limited['jobs'],
    #      },
    #      indent=4, 
    #      sort_keys=True,
    #  )
    #)

    #---------------------------------------
    # return dict with data
    #---------------------------------------
    #print("****** DEBUG: jobs_limited = ")
    #print(json.dumps(jobs_limited,indent=4))
    return {
        'jobs': jobs_limited['jobs'],
        'last_job_num': last_job_num,
    }

from flask import render_template,request
from app import app,load_jobs
import json


#-------------------------
# vars
#-------------------------
stash = {
    'app_ver': '0.0.17',
}


#-------------------------
# frontend UI endpoints
#-------------------------
@app.route('/')
@app.route('/index')
def index():
    #app_ver = '0.0.10'
    return render_template(
        'index.html',
        stash = stash,
    )

@app.route('/inventory')
def inventory():
    return render_template(
        'inventory.html',
        stash = stash,
    )

@app.route('/playbooks')
def playbooks():
    return render_template(
        'playbooks.html',
        stash = stash,
    )

@app.route('/roles')
def roles():
    return render_template(
        'roles.html',
        stash = stash,
    )

@app.route('/jobs')
def jobs():
    return render_template(
        'jobs.html',
        stash = stash,
    )

#-------------------------
# backend runner endpoints
#-------------------------
@app.route('/api')
def api():
    return json.dumps(
        {
            "error": "not implemented", 
        },
        indent=4,
    )

@app.route('/api/get_jobs')
def get_jobs():
    return json.dumps(
	load_jobs.load_jobs(
            requested_num=5
        ),
        indent=4,
    )

@app.route('/api/run_job')
def run_job():
    return 'not yet implemented'

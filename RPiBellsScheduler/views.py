"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, request, url_for
from RPiBellsScheduler import app
from RPiBellsScheduler.bellsscheduler import BellssScheduler


@app.route('/')
@app.route('/bells_scheduler', methods=['GET'])
def bells_scheduler():
    """Renders the home page with scheduled tasks."""
    return render_template(
        'index.html',
        jobs=BellssScheduler.find_bells_schedule_by_command()
    )

@app.route('/add-job-bell', methods=['GET', 'POST'])
def add_job_bell():
    """Render the adding job page."""
    if request.method == 'POST':
        req = request.form
        m = req.get("inputMin")
        h = req.get("inputHour")
        dom = req.get("inputDOM")
        mon = req.get("inputMON")
        dow = req.get("inputDOW")

        # Prepare time slice for task.
        task_schedule = BellssScheduler.replace_zero("{0} {1} {2} {3} {4}".format(m, h, dom, mon, dow), "*")

        BellssScheduler.create_new_job(task_schedule)
        return redirect(
            url_for('bells_scheduler')
        )
    else:
        return render_template(
            'add-job-bell.html'
        )

@app.route('/delete-job-bell/<string:m>/<string:h>/<string:dom>/<string:mon>/<string:dow>',
          methods=['POST'])
def delete_job_bell(m, h, dom, mon, dow):
    """Delete an existing task by schedule."""
    task_schedule = "{0} {1} {2} {3} {4}".format(m, h, dom, mon, dow)
    BellssScheduler.remove_existed_job_by_time(task_schedule)

    return redirect(
        url_for('bells_scheduler')
    )

@app.route('/terms-of-use', methods=['GET'])
def terms_of_use():
    """Renders the about page."""
    return render_template(
        'terms-of-use.html',
        title='Terms of Use',
        year=datetime.now().year,
        message='The terms of use of the application .'
    )

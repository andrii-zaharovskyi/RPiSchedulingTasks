#!/usr/bin/python3
#-*- encoding: utf-8 -*-

"""
Contains the class for interacting with Cron.
"""

import re
import sys
from crontab import CronTab
from config import COMMAND, CRON_USER


class BellssScheduler(object):
    """
    Represents functionality for configuring scheduled tasks via Cron tool.
    """

    # Private static variable that stores the CronTab instance.
    global _cron_tab
    _cron_tab = CronTab(user=CRON_USER)

    def find_bells_schedule_by_command():
        """Find an existing tasks by command. Return list of tasks."""
        jobs_list = []
        iter = _cron_tab.find_command(COMMAND)
        print(COMMAND) 

        for job in iter:
            job_rep = {
                'm': job.minutes,
                'h': job.hours,
                'dom': job.dom,
                'mon': job.months,
                'dow': job.dow,
                'command': job.command
            }
            jobs_list.append(job_rep) 
        return jobs_list

    def create_new_job(task_schedule: str):
        """Create new task in Cron."""
        try:
            # Creating a job with a comment.
            job = _cron_tab.new(command=COMMAND)
        
            # Setting all time slices at once (e.g.: '2 10 * * *').
            job.setall(task_schedule)

            # Validity check.
            if job.is_valid():
                job.enable()
                _cron_tab.write()
            return(True, "The task was created successfully.")
        except:
            return((False, sys.exc_info()[0]))

    def remove_existed_job_by_time(task_schedule: str):
        """Remove items from Cron."""
        try:
            # Find an existing job by schedule.
            jobs = _cron_tab.find_time(task_schedule)
            _cron_tab.remove(jobs)
            # Write CronTab back to system.
            _cron_tab.write()
            return((True, "The task was removed successfully"))
        except:
            return((False, sys.exc_info()[0]))

    def replace_zero(string: str, repl: str):
        """ Return the string obtained by replacing the leftmost non-overlapping  
        occurrences of pattern in string by the replacement repl.
        """
        pattern = r'(\b0{1}\b)'
        repl = "*"
        return re.sub(pattern, repl, string)

#!/usr/bin/python3
#-*- encoding: utf-8 -*-

import os


# Specify the command for execute as a routine task.
COMMAND = 'python3 {}'.format(os.path.abspath('bell.py'))

# Specify the command for crontab on RaspberryPi.
CRON_USER = 'pi'

# Specify the pin numbers for the bell module. 
PIN_IN2 = 33
PIN_IN3 = 35
PIN_IN4 = 37

# Specify waiting time (seconds).
TIMEOUT = 2

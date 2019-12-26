#!/usr/bin/python3
#-*- encoding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
from config import *


def main():
    # Initialize a board for working.
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # Initialize the ports and their actions.
    GPIO.setup(PIN_IN2, GPIO.OUT)
    GPIO.setup(PIN_IN3, GPIO.OUT)
    GPIO.setup(PIN_IN4, GPIO.OUT)

    # Turn on all ports.
    GPIO.output(PIN_IN2, 0)
    GPIO.output(PIN_IN3, 0)
    GPIO.output(PIN_IN4, 0)

    # Waiting some second befor turning off the ports.
    sleep(TIMEOUT)

    # Turn off all ports.
    GPIO.output(PIN_IN2, 1)
    GPIO.output(PIN_IN3, 1)
    GPIO.output(PIN_IN4, 1)

     # Clean up all pins which use.
    GPIO.cleanup() 


if __name__ == "__main__":
    main()

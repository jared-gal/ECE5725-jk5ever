#! /usr/bin/python

import RPi.GPIO as GPIO
import time
import subprocess
import sys

#setting up all gpio pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.IN)

#callbacks for each of the buttons and their corresponding actions
def gpio17(channel):
    cmd = "echo seek -10 0  > /tmp/mplayer-fifo"
    print subprocess.check_output(cmd, shell=True)

def gpio22(channel):
    cmd = "echo seek 10 0  > /tmp/mplayer-fifo"
    print subprocess.check_output(cmd, shell=True)

def gpio23(channel):
    cmd = "echo seek -30 0  > /tmp/mplayer-fifo"
    print subprocess.check_output(cmd, shell=True)

def gpio27(channel):
    cmd = "echo seek 30 0  > /tmp/mplayer-fifo"
    print subprocess.check_output(cmd, shell=True)

def gpio26(channel):
    cmd = "echo pause  > /tmp/mplayer-fifo"
    print subprocess.check_output(cmd, shell=True)

def gpio19(channel):
    cmd = "echo quit  > /tmp/mplayer-fifo"
    print subprocess.check_output(cmd, shell=True)
    sys.exit()
    GPIO.cleanup()


if __name__ == "__main__":

	#setting up callbacks for the buttons
    GPIO.add_event_detect(17, GPIO.FALLING, callback = gpio17, bouncetime =300)	
    GPIO.add_event_detect(22, GPIO.FALLING, callback = gpio22, bouncetime =300)
    GPIO.add_event_detect(23, GPIO.FALLING, callback = gpio23, bouncetime =300)
    GPIO.add_event_detect(27, GPIO.FALLING, callback = gpio27, bouncetime =300)
    GPIO.add_event_detect(26, GPIO.RISING, callback = gpio26, bouncetime =300)
    GPIO.add_event_detect(19, GPIO.RISING, callback = gpio19, bouncetime =300)

    while 1:
        time.sleep(1)
        


	

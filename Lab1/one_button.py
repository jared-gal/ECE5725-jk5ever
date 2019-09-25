#! /usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
button = 1

while(1):
    button = GPIO.input(17)
    if(button == 0):
        print "BUTTON 17 IS PRESSED"
    time.sleep(.1)


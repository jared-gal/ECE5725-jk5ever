#! /usr/bin/python
import RPi.GPIO as GPIO

import os
import time 
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb0')

#setting up GPIO pin to run the calibration signal with f = 46.51 and duty cycle = 6.977%
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
servo_pin = GPIO.PWM(5, 46.51)
servo_pin.start(6.977)

#reading user input as to when to end the program
usr_in = "cat"
while (usr_in != "done"):
    usr_in = raw_input("type done when done")
    time.sleep(.01)

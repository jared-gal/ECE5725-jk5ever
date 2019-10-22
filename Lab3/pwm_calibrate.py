#! /usr/bin/python
import RPi.GPIO as GPIO

import os
import time 
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb0')

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)
servo_pin = GPIO.PWM(5, 46.51)
servo_pin.start(6.977)


usr_in = "cat"
while (usr_in != "done"):
    usr_in = raw_input("type done when done")
    time.sleep(.01)

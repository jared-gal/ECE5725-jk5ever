#! /usr/bin/python
import RPi.GPIO as GPIO

import os
import time 
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb0')

#setting up gpio pin for pwm
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
led_pin = GPIO.PWM(4, 1)
led_pin.start(50)

#taking user input to change the frequency of the PWM signal
while(1):
    usr_in = 1
    usr_in = raw_input("Enter a Frequency: \n")
    led_pin.ChangeFrequency(int(usr_in))
    time.sleep(.01)

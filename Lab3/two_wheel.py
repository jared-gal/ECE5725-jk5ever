#! /usr/bin/python

import RPi.GPIO as GPIO
import time
import subprocess
import sys, os


# touchscreen stuff
os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1') #

#SETUP FOR GPIO BUTTONS
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

#BUTTONS FOR THE LEFT SERVO
def gpio17(channel):
    servo_pinL.ChangeFrequency(46.51)
    servo_pinL.ChangeDutyCycle(6.977)

def gpio22(channel):
    servo_pinL.ChangeFrequency(46.95)
    servo_pinL.ChangeDutyCycle(6.1)

def gpio23(channel):
    servo_pinL.ChangeFrequency(46.08)
    servo_pinL.ChangeDutyCycle(7.83)

#BUTTONS FOR THE RIGHT SERVO
def gpio27(channel):
    servo_pinR.ChangeFrequency(46.51)
    servo_pinR.ChangeDutyCycle(6.977)
    print("27")

def gpio26(channel):
    servo_pinR.ChangeFrequency(46.95)
    servo_pinR.ChangeDutyCycle(6.1)
    print("26")

def gpio19(channel):
    servo_pinR.ChangeFrequency(46.08)
    servo_pinR.ChangeDutyCycle(7.83)
    print("19")


if __name__ == "__main__":

    #setting up callback events for each button
    GPIO.add_event_detect(17, GPIO.FALLING, callback = gpio17, bouncetime =300) 
    GPIO.add_event_detect(22, GPIO.FALLING, callback = gpio22, bouncetime =300)
    GPIO.add_event_detect(23, GPIO.FALLING, callback = gpio23, bouncetime =300)
    GPIO.add_event_detect(27, GPIO.FALLING, callback = gpio27, bouncetime =300)
    GPIO.add_event_detect(26, GPIO.RISING, callback = gpio26, bouncetime =300)
    GPIO.add_event_detect(19, GPIO.RISING, callback = gpio19, bouncetime =300)

    #initializing PWM on pin 4
    servo_pinL = GPIO.PWM(4, 46.51)
    servo_pinL.start(6.977)

    #initializing PWM on pin5
    servo_pinR = GPIO.PWM(5, 46.51)
    servo_pinR.start(6.977)

    while 1:
        time.sleep(1)
        


    

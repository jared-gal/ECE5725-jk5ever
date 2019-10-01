#! /usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.IN)

button1 = 1
button2 = 1
button3 = 1
button4 = 1
button5 = 0
button6 = 0

while(1):
    button1 = GPIO.input(17)
    button2 = GPIO.input(22)
    button3 = GPIO.input(23)
    button4 = GPIO.input(27)
    button5 = GPIO.input(26)
    button6 = GPIO.input(19)

    if(button1 == 0):
        print "BUTTON 17 IS PRESSED"  
    if(button2 == 0):
        print "BUTTON 22 IS PRESSED"
    if(button3 == 0):
        print "BUTTON 23 IS PRESSED"
    if(button4 == 0):
        print "BUTTON 27 IS PRESSED"
    if(button5 == 1):
        print "BUTTON 26 IS PRESSED"
    if(button6 == 1):
        print "BUTTON 19 IS PRESSED"

        break
        
    time.sleep(.1)


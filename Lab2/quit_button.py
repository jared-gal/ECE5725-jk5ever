#! /usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def quitCallback(channel):
    sys.exit()


if __name__ == "__main__":

    GPIO.add_even_detect(27, GPIO.FALLING, callback= quitCallback, bouncetime=300)
    
    while(1):

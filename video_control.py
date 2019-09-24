#! /usr/bin/python

import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)




def case_eval(button):
    switcher = {
        9:"pause",
        8:"seek 10 0",
        7:"seek -10 0",
        6:"quit",
        10:""
    }
    return switcher.get(button,"Invalid Command")

if __name__ == "__main__":

	button1 = 1
	button2 = 1
	button3 = 1
	button4 = 1
	
        
        command = " cat"

	while(command != "quit"):
	    button1 = GPIO.input(17)
	    button2 = GPIO.input(22)
	    button3 = GPIO.input(23)
	    button4 = GPIO.input(27)

	    button = button1 + button2*2 + button3*3 + button4*4
	    command = case_eval(button)
            
            if(command != "Invalid Command"):
	    	cmd = "echo "+command+" > /tmp/mplayer-fifo"
            	print subprocess.check_output(cmd, shell=True)
	    else:
                print command

	    time.sleep(.1)
	

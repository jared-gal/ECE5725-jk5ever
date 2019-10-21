#! /usr/bin/python

import RPi.GPIO as GPIO
import time
import subprocess

#getting the start time
st = time.time()

#setting up the buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.IN)

#eval function for button presses
def case_eval(button):
    switcher = {
        15:"seek -30 0",
        16:"seek 30 0",
        17:"quit",
        18:"seek -10 0",
        19:"seek 10 0",
        20:"pause",
        21:""
    }
    return switcher.get(button,"Invalid Command")

if __name__ == "__main__":

	#base state of buttons
	button1 = 1
	button2 = 1
	button3 = 1
	button4 = 1
        button5 = 1
        button6 = 1
	
        
        command = " cat"
	
	#run polling algo for 10 seconds for comparison with perf
	while((time.time()-st) < 10):
		
	    #same button logic as before
	    button1 = GPIO.input(17)
	    button2 = GPIO.input(22)
	    button3 = GPIO.input(23)
	    button4 = GPIO.input(27)
            button5 = GPIO.input(26)
            button6 = GPIO.input(19)
	
	    button = button1 + button2*2 + button3*3 + button4*4 + (1-button5)*5 + (1-button6)*6
	    command = case_eval(button)
            
            if(command != "Invalid Command" and command != ""):
	    	cmd = "echo "+command+" > /tmp/mplayer-fifo"
            	print subprocess.check_output(cmd, shell=True)
	    

#! /usr/bin/python
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
import os, sys
import time

# touchscreen stuff
os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1') #
os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

#SETUP FOR GPIO BUTTONS
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

#BUTTONS FOR THE LEFT SERVO
update_hist_left = False
update_hist_right = False
left_dir  = "STOP"
left_time = 0
right_dir  = "STOP"
right_time = 0

#pygame setup basics
pygame.init()
#pygame.mouse.set_visible(False)
size = width, height = 320, 240
screen = pygame.display.set_mode(size)
WHITE = 255,255,255,255
BLACK = 0,0,0
RED = 255,0,0
GREEN = 0,255,0

#setting up buttons and blacking out the screen
my_fontB = pygame.font.Font(None, 50)
my_fontS = pygame.font.Font(None, 25)
my_buttons_cont = {'CONT':(160,120),'quit':(280, 200)}
my_buttons_stop = {'STOP':(160,120),'quit':(280, 200)}
my_buttons_start = {'START':(160,120), 'quit':(280,200)}

screen.fill(BLACK)


if __name__ == "__main__":
    #setting up the base histories
    #__________________________________________________________- 
    left_1_R = my_fontS.render('STOP, 0', True, WHITE)
    left_1   = left_1_R.get_rect(center=(40,100))
    left_2_R = my_fontS.render('STOP, 0', True, WHITE)
    left_2   = left_1_R.get_rect(center=(40,133))
    left_3_R = my_fontS.render('STOP, 0', True, WHITE)
    left_3   = left_1_R.get_rect(center=(40,166))  
    
    right_1_R = my_fontS.render('STOP, 0', True, WHITE)
    right_1   = right_1_R.get_rect(center=(280,100))
    right_2_R = my_fontS.render('STOP, 0', True, WHITE)
    right_2   = right_1_R.get_rect(center=(280,133))
    right_3_R = my_fontS.render('STOP, 0', True, WHITE)
    right_3   = right_1_R.get_rect(center=(280,166))
    
    screen.blit(left_1_R, left_1)
    screen.blit(left_1_R, left_2)
    screen.blit(left_1_R, left_3)
    screen.blit(right_1_R, right_1)
    screen.blit(right_1_R, right_2)
    screen.blit(right_1_R, right_3)
        
    #initializing PWM on pin 4
    servo_pinL = GPIO.PWM(4, 46.51)
    servo_pinL.start(0)

    #initializing PWM on pin5
    servo_pinR = GPIO.PWM(5, 46.51)
    servo_pinR.start(0)
    
    #state variable to define what is happening: 0 - just started, 1 - stopped, 2 - going straight, 3 - going back, 4 - turn left, 5 - turn right
    state = 0

    #to record what state we were in before emergency stopping and duration through it
    last_state = 0 
    stopped_time = 0

    #whether or not quit button was hit
    Quit = False

    #what buttons are to be displayed
    my_buttons = my_buttons_start
    
    while(not Quit):
        time.sleep(.01)
        #update rectangles
        
        if (update_hist_left):
            left_time = round(time.time()-start_time)
        
            left_3_R = left_2_R
            left_2_R = left_1_R
            
            
            left_2   = left_2_R.get_rect(center=(40,133))
            left_3   = left_3_R.get_rect(center=(40,166))
            
            
            left_1_R = my_fontS.render(left_dir+", "+str(left_time), True, WHITE)
            left_1 = left_1_R.get_rect(center=(40,100))
            
            
            
           
            
            update_hist_left = False
            
            
        if (update_hist_right):
            right_time = round(time.time()-start_time)
            right_3_R = right_2_R
            right_2_R = right_1_R
            
            right_2   = right_2_R.get_rect(center=(280,133))
            right_3   = right_3_R.get_rect(center=(280,166))
            
            right_1_R = my_fontS.render(right_dir+", "+str(right_time), True, WHITE)
            right_1 = right_1_R.get_rect(center=(280,100))
            
            
            update_hist_right = False
            
        screen.fill(BLACK)
        screen.blit(left_1_R, left_1)
        screen.blit(left_2_R, left_2)
        screen.blit(left_3_R, left_3)
        screen.blit(right_1_R, right_1)
        screen.blit(right_2_R, right_2)
        screen.blit(right_3_R, right_3)
        
    
        
        for event in pygame.event.get(): 
            if(event.type is MOUSEBUTTONDOWN): 
                pos = pygame.mouse.get_pos()
            elif(event.type is MOUSEBUTTONUP):
                pos = pygame.mouse.get_pos()
                x,y = pos

                if y>175: 
                    if x>255: 
                        Quit = True
                elif y<145 and y>95 and x>135 and x<185:
                    if not(state == 1):
                        my_buttons = my_buttons_cont
                       
			last_state = state
			stop_time = dur
			state == 1
                    else:
                        my_buttons = my_buttons_stop
                    	state = last_state
			dur = stop_time

        if state == 0:
	    my_buttons = my_buttons_start
	    #update freq and duty to be 0 for both  
            pygame.draw.circle(screen, RED, [160,120], 60)
        elif state ==1:
	    #update history to have new stop term
	    #set duty cycle to be 0
	elif state ==2:
	    #update history with forward entries for L and R (ccw and CW)
	    #set appropriate speeds to be half max
	elif state ==3:
	   #
	elif state ==4:

	elif state ==5:

        else:





            pygame.draw.circle(screen, GREEN, [160,120], 60)
            servo_pinL.ChangeFrequency(46.51)
            servo_pinL.ChangeDutyCycle(6.977)
            servo_pinR.ChangeFrequency(46.51)
            servo_pinR.ChangeDutyCycle(6.977)
            
        for my_text, text_pos in my_buttons.items():
            text_surface = my_fontB.render(my_text, True, WHITE)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)

        pygame.display.flip()

	#start of FSM
	


    GPIO.cleanup()


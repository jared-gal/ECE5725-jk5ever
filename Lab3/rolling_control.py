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
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

#BUTTONS FOR THE LEFT SERVO
update_hist_left = False
update_hist_right = False
left_dir  = "STOP"
left_time = 0
right_dir  = "STOP"
right_time = 0
start_time = time.time()

#left servo stop
def gpio17(channel):
    global update_hist_left
    global left_dir
    #handling the change of duty cycle as well as flagging to update
    #the scrolling history with the new command
    servo_pinL.ChangeDutyCycle(0)
    update_hist_left = True
    left_dir  = "STOP"
    
#left servo CW
def gpio22(channel):
    global update_hist_left
    global left_dir
    #handling the change of duty cycle/freqeuncy as well as flagging to update
    #the scrolling history with the new command
    servo_pinL.ChangeFrequency(46.95)
    servo_pinL.ChangeDutyCycle(6.1)
    update_hist_left = True
    left_dir  = "CW"

#left servo CCW
def gpio23(channel):
    global update_hist_left
    global left_dir
    #handling the change of duty cycle/freqeuncy as well as flagging to update
    #the scrolling history with the new command
    servo_pinL.ChangeFrequency(46.08)
    servo_pinL.ChangeDutyCycle(7.83)
    update_hist_left = True
    left_dir  = "CCW"
    
#BUTTONS FOR THE RIGHT SERVO
def gpio27(channel):
    global update_hist_right
    global right_dir
    #handling the change of duty cycle as well as flagging to update
    #the scrolling history with the new command
    servo_pinR.ChangeDutyCycle(0)
    update_hist_right = True
    right_dir  = "STOP"

def gpio26(channel):
    global update_hist_right
    global right_dir
    #handling the change of duty cycle/freqeuncy as well as flagging to update
    #the scrolling history with the new command
    servo_pinR.ChangeFrequency(46.95)
    servo_pinR.ChangeDutyCycle(6.1)
    update_hist_right = True
    right_dir  = "CW"

def gpio19(channel):
    global update_hist_right
    global right_dir
    #handling the change of duty cycle/freqeuncy as well as flagging to update
    #the scrolling history with the new command
    servo_pinR.ChangeFrequency(46.08)
    servo_pinR.ChangeDutyCycle(7.83)
    update_hist_right = True
    right_dir  = "CCW"


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
my_buttons_stop = {'CONT':(160,120),'quit':(280, 200)}
my_buttons_go = {'STOP':(160,120),'quit':(280, 200)}


screen.fill(BLACK)


if __name__ == "__main__":
    #setting up callback events for each button
    GPIO.add_event_detect(17, GPIO.FALLING, callback = gpio17, bouncetime =300) 
    GPIO.add_event_detect(22, GPIO.FALLING, callback = gpio22, bouncetime =300)
    GPIO.add_event_detect(23, GPIO.FALLING, callback = gpio23, bouncetime =300)
    GPIO.add_event_detect(27, GPIO.FALLING, callback = gpio27, bouncetime =300)
    GPIO.add_event_detect(26, GPIO.RISING, callback = gpio26, bouncetime =300)
    GPIO.add_event_detect(19, GPIO.RISING, callback = gpio19, bouncetime =300)
    
    #initializing the rolling history for left wheel
    left_1_R = my_fontS.render('STOP, 0', True, WHITE)
    left_1   = left_1_R.get_rect(center=(40,100))
    left_2_R = my_fontS.render('STOP, 0', True, WHITE)
    left_2   = left_1_R.get_rect(center=(40,133))
    left_3_R = my_fontS.render('STOP, 0', True, WHITE)
    left_3   = left_1_R.get_rect(center=(40,166))
    
    #initializing the rolling history for right wheel
    right_1_R = my_fontS.render('STOP, 0', True, WHITE)
    right_1   = right_1_R.get_rect(center=(280,100))
    right_2_R = my_fontS.render('STOP, 0', True, WHITE)
    right_2   = right_1_R.get_rect(center=(280,133))
    right_3_R = my_fontS.render('STOP, 0', True, WHITE)
    right_3   = right_1_R.get_rect(center=(280,166))
    
    #bliting the initila histories
    screen.blit(left_1_R, left_1)
    screen.blit(left_1_R, left_2)
    screen.blit(left_1_R, left_3)
    screen.blit(right_1_R, right_1)
    screen.blit(right_1_R, right_2)
    screen.blit(right_1_R, right_3)
        
    #initializing PWM on pin 4
    servo_pinL = GPIO.PWM(4, 46.51)
    servo_pinL.start(6.977)

    #initializing PWM on pin5
    servo_pinR = GPIO.PWM(5, 46.51)
    servo_pinR.start(6.977)
    
    #whether wheels are stopped or going
    stopped = True
    Quit = False
    my_buttons = my_buttons_go
    
    #loop to handle continuously updating screen and reading button presses on TFT
    while(not Quit):
        time.sleep(.01)
        #update rectangles
        #update left scrolling history if the flag is changed
        if (update_hist_left):
            left_time = round(time.time()-start_time)
            left_3_R = left_2_R
            left_2_R = left_1_R
            left_2   = left_2_R.get_rect(center=(40,133))
            left_3   = left_3_R.get_rect(center=(40,166))
            left_1_R = my_fontS.render(left_dir+", "+str(left_time), True, WHITE)
            left_1 = left_1_R.get_rect(center=(40,100))
            update_hist_left = False
            
        #update right scrolling history if the flag is changed    
        if (update_hist_right):
            right_time = round(time.time()-start_time)
            right_3_R = right_2_R
            right_2_R = right_1_R
            right_2   = right_2_R.get_rect(center=(280,133))
            right_3   = right_3_R.get_rect(center=(280,166))
            right_1_R = my_fontS.render(right_dir+", "+str(right_time), True, WHITE)
            right_1 = right_1_R.get_rect(center=(280,100))
            update_hist_right = False
        
        #blitting the new histories to the screen
        screen.fill(BLACK)
        screen.blit(left_1_R, left_1)
        screen.blit(left_2_R, left_2)
        screen.blit(left_3_R, left_3)
        screen.blit(right_1_R, right_1)
        screen.blit(right_2_R, right_2)
        screen.blit(right_3_R, right_3)
        
    
        #reading screen button presses
        for event in pygame.event.get(): 
            if(event.type is MOUSEBUTTONDOWN): 
                pos = pygame.mouse.get_pos()
            elif(event.type is MOUSEBUTTONUP):
                pos = pygame.mouse.get_pos()
                x,y = pos
                #quit button hit
                if y>175: 
                    if x>255: 
                        Quit = True
                #stop/resume button hit
                elif y<145 and y>95 and x>135 and x<185:
                    if stopped:
                        my_buttons = my_buttons_stop
                        
                    else:
                        my_buttons = my_buttons_go
                    stopped = not stopped
        #drawing the correct color circle and then stopping the rolling if the stop button is hit
        if stopped:
            pygame.draw.circle(screen, RED, [160,120], 60)
            
        else:
            pygame.draw.circle(screen, GREEN, [160,120], 60)
            servo_pinL.ChangeDutyCycle(0)
            servo_pinR.ChangeDutyCycle(0)
        #displaying appropriate button set based on state (stopped or not)   
        for my_text, text_pos in my_buttons.items():
            text_surface = my_fontB.render(my_text, True, WHITE)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)

        pygame.display.flip()
    GPIO.cleanup()


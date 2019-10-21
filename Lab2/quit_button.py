#! /usr/bin/python
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
import os, sys

# touchscreen stuff
os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1') #
os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')


#pygame setup basics
pygame.init()
#pygame.mouse.set_visible(False)
size = width, height = 320, 240
screen = pygame.display.set_mode(size)
WHITE = 255,255,255,255
BLACK = 0,0,0

#setting up font for quit button
my_font = pygame.font.Font(None, 50)
my_buttons = {'quit':(40, 40)}
screen.fill(BLACK)

#setting up a physical kill button
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#quit callback
def quitCallback(channel):
    sys.exit()


if __name__ == "__main__":

    #callback to quit if button pressed
    GPIO.add_event_detect(27, GPIO.FALLING, callback= quitCallback, bouncetime=300)
    
    #printing the button to the screen
    for my_text, text_pos in my_buttons.items():
    	text_surface = my_font.render(my_text, True, WHITE)
    	rect = text_surface.get_rect(center=text_pos)
    	screen.blit(text_surface, rect)
    
    pygame.display.flip()
    pos_String = "No Touch"
    quit = False
    
    #while quit button not pressed
    while(not quit):
    	for event in pygame.event.get(): 
    		if(event.type is MOUSEBUTTONDOWN): 
    			pos = pygame.mouse.get_pos()
            #on mouse press
    		elif(event.type is MOUSEBUTTONUP):
    			pos = pygame.mouse.get_pos()
    			x,y = pos
                #if clicked position is quit button then quit 
    			if y<65: 
    				if x<65: 
    					quit = True


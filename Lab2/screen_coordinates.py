#! /usr/bin/python
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
import os, sys

# touchscreen stuff
#os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
#os.putenv('SDL_FBDEV', '/dev/fb1') #
#os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
#os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')


#pygame setup basics
pygame.init()
#pygame.mouse.set_visible(False)
size = width, height = 320, 240
screen = pygame.display.set_mode(size)
WHITE = 255,255,255,255
BLACK = 0,0,0

my_font = pygame.font.Font(None, 50)
my_buttons = {'quit':(280, 200)}
screen.fill(BLACK)


GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def quitCallback(channel):
    sys.exit()


if __name__ == "__main__":

    GPIO.add_event_detect(27, GPIO.FALLING, callback= quitCallback, bouncetime=300)
    
    for my_text, text_pos in my_buttons.items():
    	text_surface = my_font.render(my_text, True, WHITE)
    	rect = text_surface.get_rect(center=text_pos)
    	screen.blit(text_surface, rect)
    pygame.display.flip()
    pos_String = "No Touch"
    quit = False
    coord_list = []
    while(not quit):
    	for event in pygame.event.get(): 
    		if(event.type is MOUSEBUTTONDOWN): 
    			pos = pygame.mouse.get_pos()
    		elif(event.type is MOUSEBUTTONUP):
    			pos = pygame.mouse.get_pos()
    			x,y = pos

    			if y>175: 
        			if x>255: 
    					quit = True
                        coord_list.append([x,y])
                        screen.fill(BLACK)
                        pos_String = "X: " + str(x) + " Y: " +str(y)
                        text_surface2=my_font.render(pos_String, True, WHITE)
                        rect2 = text_surface2.get_rect(center = (180,150))
                        screen.blit(text_surface2, rect2)
                        screen.blit(text_surface, rect) 
                        pygame.display.flip()

    for item in coord_list:
        print("X: " + str(item[0]) + " Y: " +str(item[1]))

#! /usr/bin/python
import pygame
import time
from pygame.locals import *
import RPi.GPIO as GPIO
import os, sys

# touchscreen stuff
os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1') #
os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')


#ball game stuff: speed, image loading, ball size
speed = [1, 1]
speed2 = [2, 2]
black = 0, 0, 0
ball  = pygame.image.load("golf_ball.png")
ball2 = pygame.image.load("tennis_ball.png")
ballrect  = ball.get_rect()
ballrect2 = ball2.get_rect()
ballR = 24
ball2R = 16
collision_count = 100



#pygame setup basics
pygame.init()
#pygame.mouse.set_visible(False)
size = width, height = 320, 240
screen = pygame.display.set_mode(size)
WHITE = 255,255,255,255
BLACK = 0,0,0

#menu buttons
my_font = pygame.font.Font(None, 50)
my_buttons = {'start':(40,200) ,'quit':(280, 200)}
screen.fill(BLACK)

#setting up the physical kill button
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#kill execution
def quitCallback(channel):
    sys.exit()


if __name__ == "__main__":

	#setup of kill buton callback
    GPIO.add_event_detect(27, GPIO.FALLING, callback= quitCallback, bouncetime=300)
    
	#setting up the menu buttons
    for my_text, text_pos in my_buttons.items():
    	text_surface = my_font.render(my_text, True, WHITE)
    	rect = text_surface.get_rect(center=text_pos)
    	screen.blit(text_surface, rect)
    pygame.display.flip()

    pos_String = "No Touch"
    quit = False
	#variable to see if the ball game is started
    ballGame = False

    while(not quit):
		#controlling frame rate
        time.sleep(.01)
    	for event in pygame.event.get(): 
    		if(event.type is MOUSEBUTTONDOWN): 
    			pos = pygame.mouse.get_pos()
		#on mouse press
    		elif(event.type is MOUSEBUTTONUP):
    			pos = pygame.mouse.get_pos()
    			x,y = pos
			
			#reading if quit button pressed
    			if y>175: 
        			if x>255: 
    					quit = True
			#if start button clicked
			if y>175:
				if x<65:
					ballGame = True
					
        if(ballGame):
		
		#ball collision logic drawn from ECE 4760 previous experience
		ballrect = ballrect.move(speed)
    		ballrect2 = ballrect2.move(speed2)
    		if ballrect.left < 0 or ballrect.right > width:
        		speed[0] = -speed[0]
    		if ballrect.top < 0 or ballrect.bottom > 160:
        		speed[1] = -speed[1]
    		if ballrect2.left < 0 or ballrect2.right > width:
        		speed2[0] = -speed2[0]
    		if ballrect2.top < 0 or ballrect2.bottom > 160:
        		speed2[1] = -speed2[1]

		ballcenX = (ballrect.right - ballR)
		ballcenY = (ballrect.top - ballR)
		ball2cenX = (ballrect2.right - ball2R)
		ball2cenY = (ballrect2.top - ball2R)
		    
		dx = abs(ballcenX - ball2cenX)
		dy = abs(ballcenY - ball2cenY)
    	        collision_count = max(collision_count -1,0)
		
		r_12 = [0, 0]
    		v_12 = [0, 0]
    		deltaV = [0, 0]
		
		if(dx < (ballR + ball2R) and dy < (ballR + ball2R) and collision_count == 0):
       			collision_count = 20
		        r_12[0] = dx
		        r_12[1] = dy
		
		        mag_r12 = dx*dx+dy*dy
		        v_12[0]    = speed[0] - speed2[0]
		        v_12[1]    = speed[1] - speed2[1]
		
		        dot = r_12[0]*v_12[0]+r_12[1]*v_12[1]
		
		        deltaV[0] = -dx*dot/(dx**2+dy**2)
		        deltaV[1] = -dy*dot/(dx**2+dy**2)
		
		        speed[0] = speed[0] + deltaV[0]
		        speed[1] = speed[1] + deltaV[1]
		        speed2[0] = speed2[0] - deltaV[0]
        		speed2[1] = speed2[1] - deltaV[1]

	#redrawing the balls on the screen
	screen.fill(BLACK)
	for my_text, text_pos in my_buttons.items():
    		text_surface = my_font.render(my_text, True, WHITE)
    		rect = text_surface.get_rect(center=text_pos)
    		screen.blit(text_surface, rect)
        screen.blit(ball, ballrect)
        screen.blit(ball2, ballrect2)
        pygame.display.flip()
                        

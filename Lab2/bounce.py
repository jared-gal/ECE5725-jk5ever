#! /usr/bin/python
import RPi.GPIO as GPIO

import os

#setting up for the TFT
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb1')

import sys, pygame
pygame.init()

#setting things for the pygame/movement of the ball
size = width, height = 320, 240
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

#loading up the ball to bounce
ball = pygame.image.load("magic_ball.png")
ballrect = ball.get_rect()

#setting up a button for a kill switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #moving the ball
    ballrect = ballrect.move(speed)
    
    #bouncing the ball off of walls
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    #erasing the screen and redrawing everytime
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    
    #physical kill button logic
    if(GPIO.input(27) == 0):
        break

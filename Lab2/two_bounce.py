#! /usr/bin/python
import RPi.GPIO as GPIO

import os
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb0')

import sys, pygame
pygame.init()

size = width, height = 600, 800
speed = [1, 1]
speed2 = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball  = pygame.image.load("magic_ball.png")
ball2 = pygame.image.load("baseball_ball.png")
ballrect  = ball.get_rect()
ballrect2 = ball2.get_rect()

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    ballrect2 = ballrect2.move(speed2)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    if ballrect2.left < 0 or ballrect2.right > width:
        speed2[0] = -speed2[0]
    if ballrect2.top < 0 or ballrect2.bottom > height:
        speed2[1] = -speed2[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(ball2, ballrect2)
    pygame.display.flip()
    if(GPIO.input(27) == 0):
        break

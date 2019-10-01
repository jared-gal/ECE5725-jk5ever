#! /usr/bin/python
import RPi.GPIO as GPIO

import os
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb1')

import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("magic_ball.png")
ballrect = ball.get_rect()

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    if(GPIO.input(27) == 0):
        break

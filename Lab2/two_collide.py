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

ballR = 64
ball2R = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)

collision_count = 150

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


    ballcenX = (ballrect.right - 64)
    ballcenY = (ballrect.top - 64)

    ball2cenX = (ballrect2.right - 64)
    ball2cenY = (ballrect2.top - 64)
    
    dx = abs(ballcenX - ball2cenX)
    dy = abs(ballcenY - ball2cenY)
    collision_count = max(collision_count -1,0)
    
    print("The value of BCX is %f and BCY is %f" % (ballcenX,ballcenY))

    r_12 = [0, 0]
    v_12 = [0, 0]
    deltaV = [0, 0]
    if(dx < (ballR + ball2R) and dy < (ballR + ball2R) and collision_count == 0):
       
        print("Collision")
        collision_count = 80
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


        
        '''
        tmpx = speed[0]
        tmpy=speed[1]
        speed[0] = speed2[0] #+ dv_x
        speed[1] = speed2[1] #+ dv_y
        speed2[0] = tmpx# - dv_x
        speed2[1] = tmpy# - dv_y
        '''

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(ball2, ballrect2)
    pygame.display.flip()
    if(GPIO.input(27) == 0):
        break

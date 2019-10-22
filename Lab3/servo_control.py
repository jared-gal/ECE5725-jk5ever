#! /usr/bin/python
import RPi.GPIO as GPIO

import os
import time 
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb0')

GPIO.setmode(GPIO.BCM)

#high_time = [1.48, 1.46, 1.44, 1.42,1.4,1.38, 1.36, 1.34, 1.32, 1.3]
high_time=[1.4,1.3]
high_time_ccw = [1.6,1.7]

#high_time_ccw = [1.52,1.54,1.56,1.58,1.6,1.62,1.64,1.66,1.68,1.7]

#increment_f = (max_f-stop_f)/10


GPIO.setup(4, GPIO.OUT)

#stopped to start
servo_pin = GPIO.PWM(4, 46.51)
servo_pin.start(6.977)
time.sleep(3)

for i in range(len(high_time)):
    freq = 1000/(high_time[i] + 20)
    duty = 100*high_time[i]/(high_time[i]+20)
    servo_pin.ChangeFrequency(freq)
    servo_pin.ChangeDutyCycle(duty)
    
    print("Frequencies")
    print(freq)
    print("Duty Cycle")
    print(duty)

    time.sleep(3)

for i in range(len(high_time_ccw)):
    freq = 1000/(high_time_ccw[i] + 20)
    duty = 100*high_time_ccw[i]/(high_time_ccw[i]+20)
    servo_pin.ChangeFrequency(freq)
    servo_pin.ChangeDutyCycle(duty)
    
    print("Frequencies")
    print(freq)
    print("Duty Cycle")
    print(duty)

    time.sleep(3)





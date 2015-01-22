#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

red_pin = 9
green_pin = 10
yellow_pin = 11


GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)

red = GPIO.PWM(red_pin, 100)
green = GPIO.PWM(green_pin, 100)
yellow = GPIO.PWM(yellow_pin, 100)

red.start(100)
green.start(0)
yellow.start(0)

pause_time = 0.01

try:
    while True:
        for i in range(0, 101):
            red.ChangeDutyCycle(i)
            green.ChangeDutyCycle(100-i)
            sleep(pause_time)
        for i in range(0, 101):
            green.ChangeDutyCycle(i)
            yellow.ChangeDutyCycle(100-i)
            sleep(pause_time)
        for i in range(0, 101):
            yellow.ChangeDutyCycle(i)
            red.ChangeDutyCycle(100-i)
            sleep(pause_time)

except KeyboardInterrupt:
    red.stop()
    green.stop()
    yellow.stop()
    GPIO.cleanup()
    

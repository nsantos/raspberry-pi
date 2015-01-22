#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.OUT)


def blink(pin):
    GPIO.output(pin, True)
    time.sleep(10)
    GPIO.output(pin, False)
    time.sleep(5)
    return


for i in range(1, 5):
    print 'blink',i
    blink(11)

GPIO.cleanup()
    

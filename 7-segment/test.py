#/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

digit_1 = 11

GPIO.setup(digit_1, GPIO.OUT)

i=0
while i < 11:
    GPIO.output(digit_1, True)
    sleep(2)
    GPIO.output(digit_1, True)
    i=i+1

GPIO.cleanup()

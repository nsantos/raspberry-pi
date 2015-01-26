#/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# digits activation pins
digits = (11, 3, 29, 31)

# segments activation pins
segments = (12, 13, 15, 16, 18, 19, 21, 22)

segmentDigits = [
    #a  b  c  d  e  f  g  p   Segments
    [0, 0, 0, 0, 0, 0, 1, 1], # 0
    [1, 0, 0, 1, 1, 1, 1, 1], # 1
    [0, 0, 1, 0, 0, 1, 0, 1], # 2
    [0, 0, 0, 0, 1, 1, 0, 1], # 3
    [1, 0, 0, 1, 1, 0, 0, 1], # 4
    [0, 1, 0, 0, 1, 0, 0, 1], # 5
    [0, 1, 0, 0, 0, 0, 0, 1], # 6
    [0, 0, 0, 1, 1, 1, 1, 1], # 7
    [0, 0, 0, 0, 0, 0, 0, 1], # 8
    [0, 0, 0, 0, 1, 0, 0, 1], # 9
    [0, 0, 0, 1, 0, 0, 0, 1], # A
    [1, 1, 0, 0, 0, 0, 0, 1], # b
    [0, 1, 1, 0, 0, 0, 1, 1], # C
    [1, 0, 0, 0, 0, 1, 0, 1], # d
    [0, 1, 1, 0, 0, 0, 0, 1], # E
    [0, 1, 1, 1, 0, 0, 0, 1], # F
    [1, 1, 1, 1, 1, 1, 1, 1], # blank
];


# setup all digits
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, False)

# setup all segments
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, True)

for digit in digits:
    GPIO.output(digit, True)
    for segment in segments:
        GPIO.output(segment, False)
        print 'sleeping segment'
        sleep(0.1)
    for segment in segments:
        GPIO.output(segment, True)
        print 'sleeping segment'
        sleep(0.1)
        GPIO.output(digit, True)
    GPIO.output(digit, False)
    print 'sleeping digit'
    sleep(0.2)

GPIO.cleanup()


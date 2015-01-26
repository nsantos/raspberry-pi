#/usr/bin/env python

import math
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# digits activation pins
digits = (31, 29, 3, 11)

# segments activation pins
segments = (12, 13, 15, 16, 18, 19, 21, 22)

segmentDigits2 = {
#Segment   a  b  c  d  e  f  g  p   
    '0x0':(0, 0, 0, 0, 0, 0, 1, 1),
    '0x1':(1, 0, 0, 1, 1, 1, 1, 1),
    '0x2':(0, 0, 1, 0, 0, 1, 0, 1),
    '0x3':(0, 0, 0, 0, 1, 1, 0, 1),
    '0x4':(1, 0, 0, 1, 1, 0, 0, 1),
    '0x5':(0, 1, 0, 0, 1, 0, 0, 1),
    '0x6':(0, 1, 0, 0, 0, 0, 0, 1),
    '0x7':(0, 0, 0, 1, 1, 1, 1, 1),
    '0x8':(0, 0, 0, 0, 0, 0, 0, 1),
    '0x9':(0, 0, 0, 0, 1, 0, 0, 1),
    '0xa':(0, 0, 0, 1, 0, 0, 0, 1),
    '0xb':(1, 1, 0, 0, 0, 0, 0, 1),
    '0xc':(0, 1, 1, 0, 0, 0, 1, 1),
    '0xd':(1, 0, 0, 0, 0, 1, 0, 1),
    '0xe':(0, 1, 1, 0, 0, 0, 0, 1),
    '0xf':(0, 1, 1, 1, 0, 0, 0, 1),
    '': (1, 1, 1, 1, 1, 1, 1, 1),
    }

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
    [1, 1, 0, 0, 0, 0, 1, 1], # b
    [0, 1, 1, 0, 0, 0, 1, 1], # C
    [1, 0, 0, 0, 0, 1, 0, 1], # d
    [0, 1, 1, 0, 0, 0, 0, 1], # E
    [0, 1, 1, 1, 0, 0, 0, 1], # F
    [1, 1, 1, 1, 1, 1, 1, 1], # blank
];

def setup():
    # setup all digits
    for digit in digits:
        GPIO.setup(digit, GPIO.OUT)
        GPIO.output(digit, False)

        # setup all segments
    for segment in segments:
        GPIO.setup(segment, GPIO.OUT)
        GPIO.output(segment, True)



def activate_digit(digit):
    GPIO.output(digit, True)

def deactivate_digit(digit):
    GPIO.output(digit, False)


def count(from_n, to_n):

    n_digits = (int)(math.log10(to_n)+1) #number digits from 0 usefull to index the digit position

    if n_digits < 5:
        for digit in range (n_digits):
            activate_digit(digits[digit])
            print digit
            for c in range(16):
                print c,
                for loop in range(0,7):
                    print segments[loop], bool(segmentDigits2[str(hex(c))][loop]),
                    GPIO.output(segments[loop], bool(segmentDigits2[str(hex(c))][loop]))
                print 'sleep 0.5'
                sleep(0.3)
            deactivate_digit(digits[digit])
            #sleep(1)
            #activate_digit(digit)

def count2():
    
    digit_1 = 0
    digit_2 = 0
    digit_3 = 0
    digit_4 = 0
    
    delay = 0.009

    while digit_1 < 10:
    
        print "%d %d %d %d" % (digit_4, digit_3, digit_2, digit_1)
    
        if digit_4 >= 0:
            activate_digit(digits[3])
            
            for loop in range(0,7):
                GPIO.output(segments[loop], bool(segmentDigits2[str(hex(digit_4))][loop]))
            
            sleep(delay)
            deactivate_digit(digits[3])
        
        
        if digit_3 >= 0:
            activate_digit(digits[2])
            
            for loop in range(0,7):                    
                GPIO.output(segments[loop], bool(segmentDigits2[str(hex(digit_3))][loop]))                    
        
            sleep(delay)        
            deactivate_digit(digits[2])
        
        if digit_2 >= 0:
            activate_digit(digits[1])
        
            for loop in range(0,7):                                
                GPIO.output(segments[loop], bool(segmentDigits2[str(hex(digit_2))][loop]))
        
            sleep(delay)        
            deactivate_digit(digits[1])
        
        
        if digit_1 >= 0:
            activate_digit(digits[0])
        
            for loop in range(0,7):
                GPIO.output(segments[loop], bool(segmentDigits2[str(hex(digit_1))][loop]))
        
            sleep(delay)        
            deactivate_digit(digits[0])
        
                
        if digit_1 == 9:
            digit_1 = -1
            if digit_2 == 9:
                digit_2 = -1
                if digit_3 == 9:
                    digit_3 = -1
                    if digit_4 == 9:
                        digit_4 = -1
                    digit_4 = digit_4 + 1
                digit_3 = digit_3 + 1
            digit_2 = digit_2 + 1
        digit_1 = digit_1 + 1



def main():
    setup()
    #count(0,1000)
    count2()
    GPIO.cleanup()

if __name__ == '__main__':
    main()

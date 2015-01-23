#/usr/bin/env python

import math
from time import sleep

# digits activation pins
digits = (31, 29, 3, 11)

# segments activation pins
segments = (12, 13, 15, 16, 18, 19, 21, 22)

segmentDigits2 = {
#Segment a  b  c  d  e  f  g  p   
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
    '0xb':(1, 1, 0, 0, 0, 0, 1, 1),
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
    [1, 1, 0, 0, 0, 0, 0, 1], # b
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
    pass


def count(from_n, to_n):

    n_digits = (int)(math.log10(to_n)) #number digits from 0 usefull to index the digit position

    if n_digits < 5:
        for digit in range (n_digits, -1, -1):
            activate_digit(digit)
            print digit
            for c in range(16):
                print c,
                for loop in range(0,7):
                    print segments[loop], bool(segmentDigits2[str(hex(c))][loop]),
                    #GPIO.output(segments[loop], bool(segmentDigits2[str(c)][loop])
                print 'sleep 0.05'
                sleep(0.05)
            sleep(2)

        
def main():
    count(0,1000)


if __name__ == '__main__':
    main()

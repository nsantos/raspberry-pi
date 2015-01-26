#!/usr/bin/env python

from time import sleep

number =  123
digit_1 = 0
digit_2 = 0
digit_3 = 0
digit_4 = 0

while digit_1 < 10:
    print "%d %d %d %d" % (digit_4, digit_3, digit_2, digit_1)
    sleep(0.2)
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


# Raspberry Pi's load on a 7-segment display
# Threaded version
import subprocess
import time
import RPi.GPIO as GPIO
import threading

# segment representation of each digit
# The original table was for some C library but I can't find it anywhere
# to give credit to the author. If you recognize it, leave me a comment please.

#   --a--
#  |     |
#  f     b
#  |     |
#   --g--
#  |     |
#  e     c
#  |     |
#   --d--  p

# segment representation of each digit
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

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
# blocks activation pins
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
# segments activation pins
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# deactivate all blocks
GPIO.output(3, False)
GPIO.output(5, False)
GPIO.output(7, False)
# deactivate all segments
GPIO.output(12, True)
GPIO.output(13, True)
GPIO.output(15, True)
GPIO.output(16, True)
GPIO.output(18, True)
GPIO.output(19, True)
GPIO.output(21, True)
GPIO.output(22, True)

blockActivationPins = [ 3, 5, 7, 11 ]
segmentPins = [ 12, 13, 15, 16, 22, 21, 19, 18 ]

# threaded class that returns current 1 minute load
class MinuteLoadThread(threading.Thread):

    load = None
    kill_received = False

    def run(self):
        while not self.kill_received:
            p = subprocess.Popen(['uptime'], stdout=subprocess.PIPE, 
                                             stderr=subprocess.PIPE)
            out, err = p.communicate()
            self.load = out.split(' ')[11]
            time.sleep(1)


# function that returns current 1 minute load
thread = MinuteLoadThread()
thread.start()

# wait for the thread until it finishes at least first run
# and can return some load
while thread.load is None:
    time.sleep(0.1)

# main loop
def run_loop():
    while True:
        minuteLoad = thread.load
        # print minuteLoad
        # load = get_minute_load()
        # load = '1.23'
        # remove decimal point from load
        loadSimplified = minuteLoad.replace('.', '');
        # position of decimal point
        decPoint = minuteLoad.find('.')

        # each block
        for segment in range(0,3):
            char = loadSimplified[segment]
            # appropriate segments to lit for this digit
            segmentsToLit = segmentDigits[int(char)]

            # activate block
            GPIO.output(blockActivationPins[segment], True)

            # set decimal point
            if segment == decPoint - 1:
                GPIO.output(segmentPins[7], False)
            else:
                GPIO.output(segmentPins[7], True)

            # iterate all segments in this block
            for led in range(0, 7):
                # True or False based on segmentDigits table
                val = bool(segmentsToLit[led])
                GPIO.output(segmentPins[led], val)

            # short pause
            time.sleep(0.005)

            # deactivate block
            GPIO.output(blockActivationPins[segment], False)

try:
    run_loop();
except KeyboardInterrupt:
    thread.kill_received = True

# deactivate all GPIO pins
GPIO.cleanup()


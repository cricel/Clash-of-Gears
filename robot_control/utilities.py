import RPi.GPIO as GPIO
import time
import signal
import sys
# import threading

class Utilities():
    def __init__(self):
        self.TRIC = 23
        self.ECHO = 24

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TRIC, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        GPIO.output(self.TRIC, False)

        # self.distance = 0
    
    def distance_update_once(self):
        try:
            GPIO.output(self.TRIC, True)
            time.sleep(0.00001)
            GPIO.output(self.TRIC, False)

            while GPIO.input(self.ECHO) == 0:
                pulse_start = time.time()

            while GPIO.input(self.ECHO) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 2)
            return distance
            # print (self.distance)
        except:
            pass

def signal_handler(sig, frame):
    print('clean up')
    GPIO.cleanup()
    sys.exit(0)

if __name__=="__main__": 
    signal.signal(signal.SIGINT, signal_handler)
    utilities = Utilities()
    while(True):
        print (utilities.distance_update_once())
        time.sleep(0.1)
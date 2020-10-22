import RPi.GPIO as GPIO          
from time import sleep
import signal
import sys
# import pynput

from dc_driver import *
from utilities import *
import threading

command = 'l'
dc_driver = DC_Driver()
utilities = Utilities()

def signal_handler(sig, frame):
    print('clean up')
    GPIO.cleanup()
    sys.exit(0)

def get_input():
    while(True):
        command = raw_input()
        dc_driver.update_once(command)

if __name__=="__main__": 
    signal.signal(signal.SIGINT, signal_handler)
    
    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()

    # utilities.run()
    
    distance = 0

    while(True):
        distance = utilities.distance_update_once()
        print (distance)
        time.sleep(0.1)


    
    
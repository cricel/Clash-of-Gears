import RPi.GPIO as GPIO          
from time import sleep
import signal
import sys
# import pynput

from dc_driver import *
from utilities import *
from servo import *
import threading

command = 'l'
dc_driver = DC_Driver()
servo = Servo()

def signal_handler(sig, frame):
    print('clean up')
    GPIO.cleanup()
    sys.exit(0)

def motion_left_open():
    angles = [65]
    servo.skill_motion(angles, 1)

def motion_left_close():
    angles = [0]
    servo.skill_motion(angles, 1)

def motion_right_open():
    angles = [65]
    servo.skill_motion(angles, 2)

def motion_right_close():
    angles = [0]
    servo.skill_motion(angles, 2)

def bottom_down():
    angles = [65]
    servo.skill_motion(angles, 3)

def bottom_up():
    angles = [0]
    servo.skill_motion(angles, 3)


if __name__=="__main__": 
    signal.signal(signal.SIGINT, signal_handler)

    while(True):
        command = raw_input()
        dc_driver.update_once(command)

        if (command == 'y'):
            print ("motion_left_open")
            motion_left_open_thread = threading.Thread(target=motion_left_open)
            motion_left_open_thread.daemon = True
            motion_left_open_thread.start()

        elif (command == 'u'):
            print ("motion_left_close")
            motion_left_close_thread = threading.Thread(target=motion_left_close)
            motion_left_close_thread.daemon = True
            motion_left_close_thread.start()
        
        elif (command == 'i'):
            print ("motion_right_open")
            motion_right_open_thread = threading.Thread(target=motion_right_open)
            motion_right_open_thread.daemon = True
            motion_right_open_thread.start()

        elif (command == 'o'):
            print ("motion_right_close")
            motion_right_close_thread = threading.Thread(target=motion_right_close)
            motion_right_close_thread.daemon = True
            motion_right_close_thread.start()

        elif (command == 'j'):
            print ("bottom_up")
            bottom_up_thread = threading.Thread(target=bottom_up)
            bottom_up_thread.daemon = True
            bottom_up_thread.start()

        elif (command == 'k'):
            print ("bottom_down")
            bottom_down_thread = threading.Thread(target=bottom_down)
            bottom_down_thread.daemon = True
            bottom_down_thread.start()
    
    
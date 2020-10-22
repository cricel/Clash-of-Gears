import RPi.GPIO as GPIO
import time
import signal
import sys

class Servo():
    def __init__(self):
        SER_1 = 16 # left moter
        SER_2 = 20 # right motor
        SER_3 = 21 # bottom motor

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SER_1,GPIO.OUT)
        GPIO.setup(SER_2,GPIO.OUT)
        GPIO.setup(SER_3,GPIO.OUT)
        self.servo_1 = GPIO.PWM(SER_1, 50) #pulse 50Hz
        self.servo_2 = GPIO.PWM(SER_2, 50)
        self.servo_3 = GPIO.PWM(SER_3, 50)
        self.servo_1.start(0)
        self.servo_2.start(0)
        self.servo_3.start(0)

    def update_once(self, command):
        if (command == 'y'):
            angles = [0, 45, 90, 120, 0]
            for angle in angles:
                print (angle)
                self.servo_1.ChangeDutyCycle(2+(angle/18))
                time.sleep(0.5)
                self.servo_1.ChangeDutyCycle(0)

                time.sleep(2)

    def skill_motion(self, motionarray, motornum):
        if (motornum == 1):
            for angle in motionarray:
                self.servo_1.ChangeDutyCycle(2+(angle/18))
                time.sleep(0.5)
                self.servo_1.ChangeDutyCycle(0)

        elif (motornum == 2):
            for angle in motionarray:
                self.servo_2.ChangeDutyCycle(2+(angle/18))
                time.sleep(0.5)
                self.servo_2.ChangeDutyCycle(0)

        elif (motornum == 3):
            for angle in motionarray:
                self.servo_3.ChangeDutyCycle(2+(angle/18))
                time.sleep(0.5)
                self.servo_3.ChangeDutyCycle(0)

    def stop(self):
        self.servo_1.stop()
        self.servo_2.stop()


def signal_handler(sig, frame):
    print('clean up')
    GPIO.cleanup()
    sys.exit(0)

if __name__=="__main__": 
    signal.signal(signal.SIGINT, signal_handler)
    servo = Servo()
    # servo.update_once('y')
    # angles = [0, 65, 0]
    angles = [45, 0, 90, 45]
    # servo.skill_motion(angles, 1)
    servo.skill_motion(angles, 2)
    servo.stop()
    GPIO.cleanup()


import RPi.GPIO as GPIO          

class DC_Driver():
    def __init__(self):
        # left wheel
        self.IN_1 = 24
        self.IN_2 = 23
        # right wheel
        self.IN_3 = 17
        self.IN_4 = 27
        self.EN = 25
        self.EN_R = 22

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN_1,GPIO.OUT)
        GPIO.setup(self.IN_2,GPIO.OUT)
        GPIO.setup(self.IN_3,GPIO.OUT)
        GPIO.setup(self.IN_4,GPIO.OUT)
        GPIO.setup(self.EN,GPIO.OUT)
        GPIO.setup(self.EN_R,GPIO.OUT)
        GPIO.output(self.IN_1,GPIO.LOW)
        GPIO.output(self.IN_2,GPIO.LOW)
        GPIO.output(self.IN_3,GPIO.LOW)
        GPIO.output(self.IN_4,GPIO.LOW)

        self.power=GPIO.PWM(self.EN,1000)
        self.power_r=GPIO.PWM(self.EN_R,1000)

        self.power.start(25)
        self.power_r.start(25)

    def update_once(self, command):
        if (command == 'w'):
            GPIO.output(self.IN_1,GPIO.HIGH)
            GPIO.output(self.IN_2,GPIO.LOW)
            GPIO.output(self.IN_3,GPIO.HIGH)
            GPIO.output(self.IN_4,GPIO.LOW)
            print("forward")
        elif (command == 'x'):
            GPIO.output(self.IN_1,GPIO.LOW)
            GPIO.output(self.IN_2,GPIO.HIGH)
            GPIO.output(self.IN_3,GPIO.LOW)
            GPIO.output(self.IN_4,GPIO.HIGH)
            print("backward")
        elif (command == 'a'):
            GPIO.output(self.IN_1,GPIO.LOW)
            GPIO.output(self.IN_2,GPIO.HIGH)
            GPIO.output(self.IN_3,GPIO.HIGH)
            GPIO.output(self.IN_4,GPIO.LOW)
            print("left")
        elif (command == 'd'):
            GPIO.output(self.IN_1,GPIO.HIGH)
            GPIO.output(self.IN_2,GPIO.LOW)
            GPIO.output(self.IN_3,GPIO.LOW)
            GPIO.output(self.IN_4,GPIO.HIGH)
            print("right")
        elif (command == 's'):
            GPIO.output(self.IN_1,GPIO.LOW)
            GPIO.output(self.IN_2,GPIO.LOW)
            GPIO.output(self.IN_3,GPIO.LOW)
            GPIO.output(self.IN_4,GPIO.LOW)
            print("stop")
        else:
            pass

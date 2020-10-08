import RPi.GPIO as GPIO          
from time import sleep

'''
            In1 | In2 | In3 | In4
Forward:     1     0     0     1
Backward:    0     1     1     0
Right:       1     0     1     0
Left:        0     1     0     1
Stop:        0     0     0     0
---------------------------------
Speed:      Low | Med | High
Gear:         1     2      3
pwm:         25    50     75
'''

class Car:
    def __init__(self, enA, in1, in2, in3, in4, enB):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        
        self.dutyCycles = [25, 50, 75]
        self.gear = 0
    
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(enA,GPIO.OUT)
        GPIO.setup(self.in3,GPIO.OUT)
        GPIO.setup(self.in4,GPIO.OUT)
        GPIO.setup(enB,GPIO.OUT)
        
        self.stop()

        self.pwmA = GPIO.PWM(enA, 1000)
        self.pwmA.start(25)
        self.pwmB = GPIO.PWM(enB, 1000)
        self.pwmB.start(25)
            
    def forward(self):
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)

    def backward(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)

    def right(self):
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)

    def left(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)

    def gearUp(self):
        self.gear = min(3, self.gear+1)
        self.pwmA.ChangeDutyCycle(self.dutyCycles[self.gear-1])
        self.pwmB.ChangeDutyCycle(self.dutyCycles[self.gear-1])

    def gearDown(self):
        self.gear = max(1, self.gear-1)
        self.pwmA.ChangeDutyCycle(self.dutyCycles[self.gear-1])
        self.pwmB.ChangeDutyCycle(self.dutyCycles[self.gear-1])

    def stop(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)

    def shutdown(self):
        GPIO.cleanup()
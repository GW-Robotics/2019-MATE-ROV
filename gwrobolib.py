from adafruit_servokit import ServoKit
from time import sleep
import math
class Motor:
    kit = ServoKit(channels=16)
    def __init__(self, pin, angle=90):
        self.pin = pin
        self.angle = angle
        self.last_angle = angle
        Motor.kit.servo[pin].set_pulse_width_range(1000, 2000)
        Motor.kit.servo[pin].angle = angle

    def setSpeed(self, angle):
        self.angle = angle
        if((angle > 90 and self.last_angle < 90) or (angle < 90 and self.last_angle > 90)):
            self.stop()
            sleep(0.1)
            # print("Changing direction")
        Motor.kit.servo[self.pin].angle = angle
        self.last_angle = angle

    def stop(self):
        self.angle = 90
        Motor.kit.servo[self.pin].angle = 90

class MainMotorSystem:
    def __init__(self, start_pin=0):
        self.frontRight = Motor(start_pin)
        self.frontLeft = Motor(start_pin+1)
        self.backRight = Motor(start_pin+2)
        self.backLeft = Motor(start_pin+3)
        self.angleFR = math.pi/4
        self.angleFL = 3*math.pi/4
        self.angleBL = 5*math.pi/4
        self.angleBR = 7*math.pi/4
    
    def move(self, move_vector):
        print(move_vector)
        numpad_angle = math.atan2(move_vector[1], move_vector[0])
        move_vector_mag = math.sqrt(move_vector[0]**2+move_vector[1]**2)
        self.frontRight.setSpeed((math.cos(numpad_angle-self.angleFR))*move_vector_mag*30+90)
        self.frontLeft.setSpeed((math.cos(numpad_angle-self.angleFL))*move_vector_mag*30+90)
        self.backLeft.setSpeed((math.cos(numpad_angle-self.angleBL))*move_vector_mag*30+90)
        self.backRight.setSpeed((math.cos(numpad_angle-self.angleBR))*move_vector_mag*30+90)

class VerticalMotors:
    def __init__(self, start_pin=4, max_val = 120, min_val=60):
        self.frontRight = Motor(start_pin)
        self.frontLeft = Motor(start_pin+1)
        self.backRight = Motor(start_pin+2)
        self.backLeft = Motor(start_pin+3)
        self.max = max_val
        self.min = min_val

    def move(self, frac):
        self.frontRight.setSpeed((frac+1)*(self.max-self.min)/2+self.min)
        self.frontLeft.setSpeed((frac+1)*(self.max-self.min)/2+self.min)
        self.backRight.setSpeed((frac+1)*(self.max-self.min)/2+self.min)
        self.backLeft.setSpeed((frac+1)*(self.max-self.min)/2+self.min)
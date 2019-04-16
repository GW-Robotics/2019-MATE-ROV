from adafruit_servokit import ServoKit
from time import sleep
import math
import pygame
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

    def up(self, frac):
        self.frontRight.setSpeed(self.max*frac)
        self.frontRight.setSpeed(self.max*frac)
        self.frontRight.setSpeed(self.max*frac)
        self.frontRight.setSpeed(self.max*frac)

    def up(self, frac):
        self.frontRight.setSpeed(self.min*frac)
        self.frontRight.setSpeed(self.min*frac)
        self.frontRight.setSpeed(self.min*frac)
        self.frontRight.setSpeed(self.min*frac)

def init_joystick():

    # Initialize pygame
    pygame.init()

    #Initialize joysticks
    pygame.joystick.init()

    # Acceptable events to query the controller
    input_type = [pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP, pygame.JOYHATMOTION]

    the_joystick = pygame.joystick.Joystick(0)
    the_joystick.init()

    return the_joystick, input_type


def query_values(joystick):

    curr_vals = []

    axes = joystick.get_numaxes()
    # Values go from -1 to 1
    # 0: LStick L/R
    # 1: LStcik U/D
    # 2: R2/L2
    # 3: RStick U/D
    # 4: RStick L/R
    for i in range(axes):
        axis = joystick.get_axis(i)
        curr_vals.append(int(100*axis)+100)
        
    buttons = joystick.get_numbuttons()
    # Values are 0 or 1
    # 5: A
    # 6: B
    # 7: X
    # 8: Y
    # 9: L1
    # 10: R1
    # 11: BACK
    # 12: START
    # 13: L3
    # 14: R3
    for i in range(buttons):
        button = joystick.get_button(i)
        curr_vals.append(button)
        
    hats = joystick.get_numhats()
    # Value comes back in a tuple (x, y) from with values -1, 0, or 1
    # 15: L/R
    # 16: D/U
    for i in range(hats):
        hat = joystick.get_hat(i)
        curr_vals.append(hat[0]+1)
        curr_vals.append(hat[1]+1)

    return curr_vals
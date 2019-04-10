from adafruit_servokit import ServoKit
from time import sleep
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

# class TempSensor: 
#     def __init__(self, IN1):
#         self.input_1 = InputDevice(IN1)

#     def getTemp(self): 
#         return self.input_1.value     

# class pHsensor:
#     def __init__(self, pin):
#         self.input = InputDevice(pin)
    
#     def getPh(self):
        
#         return self.input.value  
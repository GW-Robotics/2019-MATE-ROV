from adafruit_servokit import ServoKit
class Motor:
    kit = ServoKit(channels=16)
    def __init__(self, pin, angle=90):
        self.pin = pin
        self.angle = angle
        Motor.kit[pin].set_pulse_width_range(1000, 2000)
        Motor.kit[pin] = angle

    def setSpeed(self, angle):
        self.angle = angle
        Motor.kit[self.pin] = angle

    def stop(self):
        self.angle = 90
        Motor.kit[self.pin] = angle

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
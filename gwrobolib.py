from gpiozero import OutputDevice, PWMOutputDevice, InputDevice

class pHsensor:
    def __init__(self, pin):
        self.input = InputDevice(pin)
    
    def getPh(self):
        
        return self.input.value                                     

class Motor:
    def __init__(self, PWM, speed=1):
        self.speed_pin = PWMOutputDevice(PWM)
        self.speed = speed

    def forward(self):
        self.speed_pin.value = speed        
    
    def backward(self):
        self.speed_pin.value = (-speed)

    def setSpeed(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

class TempSensor: 
    def __init__(self, IN1):
        self.input_1 = InputDevice(IN1)

    def getTemp(self): 
        return self.input_1.value     


class MotorControl:
    def __init__(self, frontLeftMotor, frontRightMotor, backLeftMotor, backRightMotor):
        self.frontLeftMotor = frontLeftMotor
        self.frontRightMotor = frontRightMotor
        self.backLeftMotor = backLeftMotor
        self.backRightMotor = backRightMotor
    
    def forward():
        self.frontLeftMotor.forward()
        self.frontRightMotor.forward()
        self.backLeftMotor.backward()
        self.backRightMotor.backward()

    def backward():
        self.frontLeftMotor.backward()
        self.frontRightMotor.backward()
        self.backLeftMotor.forward()
        self.backRightMotor.forward()
    
    def turnLeft():
        self.frontRightMotor.forward()
        self.backLeftMotor.forward()
        self.frontLeftMotor.stop()
        self.backRightMotor.stop()
    
    def turnRight():
        self.frontRightMotor.stop()
        self.backLeftMotor.stop()
        self.frontLeftMotor.forward()
        self.backRightMotor.forward()
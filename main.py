import gwrobolib.*

# This is all test code for now
motor1 = Motor(3, .5)
motor2 = Motor(4)
motor3 = Motor(16)
motor4 = Motor(12)
controller = MotorControl(motor1,motor2,motor3,motor4)
controller.forward()
motor2.setSpeed(.75)
controller.backward()

phSensorrrrr = phSensor(6)
phSensorrrrr.getPh()

thermometer1orsomething = TempSensor(7)

motor2.motorBackward()
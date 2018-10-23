from gpiozero.pins.mock import MockFactory, MockPWMPin
from gpiozero import Device
from TB6612FNG import TB6612FNG
from time import sleep

motor = TB6612FNG(14, 15, 18, 23)

def setup():
    pass

def loop():
    # Motor will go forward, stop, backward, stop, at full speed
    motor.set_speed(1)
    motor.forward()
    sleep(0.5)
    motor.stop()
    sleep(0.5)
    motor.backward()
    sleep(0.5)
    motor.stop()
    sleep(0.5)

    # Motor will go forward, stop, backward, stop, at half speed
    motor.set_speed(0.5)
    motor.forward()
    sleep(0.5)
    motor.stop()
    sleep(0.5)
    motor.backward()
    sleep(0.5)
    motor.stop()
    sleep(0.5)

setup()
while True:
    loop()

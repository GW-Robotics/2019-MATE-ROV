from TB6612FNG import TB6612FNG
from time import sleep

motor = TB6612FNG(14, 15, 18, 23)

def setup():
    motor.forward()

def loop():
    sleep(0.1)

setup()
while True:
    loop()
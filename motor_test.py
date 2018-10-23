from TB6612FNG import TB6612FNG
from time import sleep

motor = TB6612FNG(14, 15, 18, 23)

def setup():
    pass

def loop():
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

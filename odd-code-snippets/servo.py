from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.servo[0].set_pulse_width_range(1000, 2000)
kit.servo[0].angle = 90

while True:
    val = input('give angle: ')
    val = int(val)
    kit.servo[0].angle = val
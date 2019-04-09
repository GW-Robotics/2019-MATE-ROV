import socket
from time import sleep
HOST = input("Enter IP: ")  # The server's hostname or IP address
PORT = 50000        # The port used by the server

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.servo[0].set_pulse_width_range(1000, 2000)
kit.servo[0].angle = 90

# Map value x (between a and b) to value y (between c and d)


def map_values(x, a, b, c, d):
    return (x-a)*((d-c)/(b-a))+c


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to server
    s.connect((HOST, PORT))
    last_val = 90
    while True:
        # send data
        s.sendall(bytearray([1]))
        # recieve data
        data = s.recv(1024)
        # print data
        if data:
            new_data = []
            for b in data:
                new_data.append(b)
            # print(new_data)
            motor_val = map_values(new_data[3], 0, 200, 60, 120)
            if((motor_val > 90 and last_val < 90) or (motor_val < 90 and last_val > 90)):
                kit.servo[0].angle = 90
                sleep(0.1)
                print("Changing direction")
            print(motor_val)
            kit.servo[0].angle = int(motor_val)
            last_val = motor_val
        else:
            print('No data received')

# save motor values and send 90 if change of direction

import socket
from gwrobolib import Motor, MainMotorSystem
# HOST = input("Enter IP: ")  # The server's hostname or IP address
HOST = '169.254.48.79'
PORT = 50000        # The port used by the server

# Map value x (between a and b) to value y (between c and d)
def map_values(x, a, b, c, d):
    return (x-a)*((d-c)/(b-a))+c

up1 = Motor(4)
up2 = Motor(5)
up3 = Motor(6)
up4 = Motor(7)

directionalMotors = MainMotorSystem()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to server
    s.connect((HOST, PORT))
    while True:
        # send data
        s.sendall(bytearray([1]))
        # recieve data
        data = s.recv(1024)
        if data:
            new_data = []
            for b in data:
                new_data.append(b)

            print(new_data)

            directionalMotors.move([new_data[4]/100-1, (new_data[3]/100-1)])
        else:
            print('No data received')


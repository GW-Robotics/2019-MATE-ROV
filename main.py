import socket
HOST = '169.254.128.193'  # The server's hostname or IP address
PORT = 50000        # The port used by the server

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.servo[0].set_pulse_width_range(1000, 2000)
kit.servo[0].angle = 90

# Map value x (between a and b) to value y (between c and d)
def map_values(x, a, b, c, d):
    return (x-a)*((d-c)/(b-a))+c

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #connect to server
    s.connect((HOST, PORT))
     
    while True:
        #send data
        s.sendall(bytearray([1]))
        #recieve data
        data = s.recv(1024)
        #print data
        if data: 
            new_data =[]
            for b in data:
                new_data.append(b)
            print(new_data)
            motor_val = map_values(new_data[3], 0, 200, 0, 180)
            kit.servo[0].angle = int(motor_val)
        else:
            print('No data received')
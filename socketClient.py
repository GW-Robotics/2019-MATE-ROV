import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 50000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to server
    s.connect((HOST, PORT))
    # TODO: add try catch to connect 
    while True:
        #send data
        s.sendall(bytearray([1]))
        #recieve data
        data = s.recv(1024)
        #print data
        if data:  
            print(data)
        else:
            print('No data received')
        
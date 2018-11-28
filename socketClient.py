import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 50000        # The port used by the server
i=0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #connect to server
    s.connect((HOST, PORT))
    #TODO: add try catch to connect 
    while True:
        #send data
        s.sendall(bytearray([i,i+1]))
        #data stuff
        i=i+1
        if i>128:
            i=0
        #recieve data
        data = s.recv(1024)
        #print data
        if data:  
            print(data[0],data[1])
        else:
            print('No data received')
        
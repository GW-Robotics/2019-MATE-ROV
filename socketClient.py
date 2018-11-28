import socket
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 50000        # The port used by the server
i=0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(bytearray([i,i+1]))
        i=i+1
        if i>128:
            i=0
        data = s.recv(1024)
        if data:  
            print('Received', repr(data))
        else:
            print('No data received')
        
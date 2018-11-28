import socket
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 50000        # The port used by the server
i=0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)
        s.sendall(bytes([i]))
        i=i+1
        if i>256:
            i=0
        if data:
                print('Received', repr(data))
        
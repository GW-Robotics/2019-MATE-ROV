import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 50000        # Port to listen on (non-privileged ports are > 1023)
i=0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Ready to connect")
    conn, addr = s.accept()
    
    with conn:
        print('Connected by', addr)
        while True:
            conn.sendall(bytearray([i,i+1]))
            i=i+1
            if i>128:
                i=0
            data = conn.recv(1024)
            if data:  
                print('Received', repr(data))
            else:
                print('No data received')

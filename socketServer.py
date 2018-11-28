import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 50000        # Port to listen on (non-privileged ports are > 1023)
i=0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #def socket s
    s.bind((HOST, PORT))
    s.listen()
    print("Ready to connect")
    #wait for connection
    conn, addr = s.accept()
    
    with conn:
        #on connect being to send and receive data
        print('Connected by', addr)
        while True:
            #send
            conn.sendall(bytearray([i,i+1]))
            #ex data
            i=i+1
            if i>128:
                i=0
            #then recieve
            data = conn.recv(1024)
            #print data if received
            if data:  
                print(data[0],data[1])
            else:
                print('No data received')

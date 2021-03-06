import socket
#import joystick 
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 50000        # Port to listen on (non-privileged ports are > 1023)
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
            sendData = joystick.query_values()
            conn.sendall(bytearray(sendData))
            #then recieve
            data = conn.recv(1024)
            #print data if received
            if data:  
                print("I have Data")
            else:
                print('No data received')

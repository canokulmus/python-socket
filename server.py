# socket server example in python

import socket
import time

HEADERSIZE = 10

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4, SOCK_STREAM = TCP # also can use SOCK_DGRAM for UDP

# next step is to bind the socket to a host and port
# get local machine name and arbitrary port
host = socket.gethostname() 
port = 1234 
s.bind(( host, port ))

s.listen(5) # 5 is the number of connections we can have waiting at any one time

while True:
    # establish a connection
    # clientsocket is a new socket object usable to send and receive data on the connection, and addr is the address bound to the socket on the other end of the connection
    clientsocket, address = s.accept() # accept returns a tuple of two values: a new socket object representing the connection, and the address of the client
    print(f"Connection from {address} has been established!")
    
    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg 

    # send a message to the client socket
    clientsocket.send(bytes(msg, "utf-8"))

    while True: # send the time every 3 seconds
        time.sleep(3)
        msg = f"The time is! {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg 
        clientsocket.send(bytes(msg, "utf-8"))
        
        

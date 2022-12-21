# socket server example in python

import socket
import time
import pickle # for serializing and deserializing objects




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
    
    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d) # serialize the object # already in bytes

    msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg # add the header to the message in bytes

    clientsocket.send(msg) # send a message to the client socket in bytes


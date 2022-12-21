# socket server example in python

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4, SOCK_STREAM = TCP # also can use SOCK_DGRAM for UDP

s.connect((socket.gethostname(), 1234)) # connect to the server

msg = s.recv(1024) # receive 1024 bytes of data. This is the maximum amount of data that can be received at once (buffer size) # 1024 is a common buffer size
print(msg.decode("utf-8")) # decode the message from bytes to a string

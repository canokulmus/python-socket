# socket server example in python

import socket


HEADERSIZE = 10


# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4, SOCK_STREAM = TCP # also can use SOCK_DGRAM for UDP

s.connect((socket.gethostname(), 1234)) # connect to the server

while True:
    
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16) # receive 1024 bytes of data. This is the maximum amount of data that can be received at once (buffer size) # 1024 is a common buffer size
        
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}") # print the length of the message
            msglen = int(msg[:HEADERSIZE]) # get the length of the message
            new_msg = False 
        full_msg += msg.decode("utf-8") # decode the message from bytes to string
        
        # if the length of the message is equal to the length of the message we received, then we have received the full message
        if len(full_msg)-HEADERSIZE == msglen:  
            print("full msg received")
            print(full_msg[HEADERSIZE:]) # print the message without the header
            new_msg = True
            full_msg = ''
            
        
    print(full_msg)
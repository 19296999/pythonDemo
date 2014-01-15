# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   响应客户端的请求
#
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    buf = socket.recv()
    print "I receive:", buf 
 
    if buf == '1':  
       	socket.send('welcome to server!')  
    else: 
        socket.send('bye')

# <codecell>



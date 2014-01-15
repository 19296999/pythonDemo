# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   发送十次请求到服务器
#
import zmq

context = zmq.Context()

#  Socket to talk to server
print "Connecting to hello world server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for i in range (0,10):
    print "Sending request ", i,"..."
    socket.send (str(i))
    
    #  Get the reply.
    message = socket.recv()
    print "Received reply ", i, "[", message, "]"

# <codecell>


# <codecell>



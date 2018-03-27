#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import sys

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
while True:
    print("Sending request %s …")
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv()
    print("Received reply")

    print(str(sys.argv[1]))

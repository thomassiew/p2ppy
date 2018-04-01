import time
import zmq
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, "")
print("Subscribing to ")
socket.connect('tcp://127.0.0.1:2000')
while True:
    message = socket.recv()
    print("Received from %s" % message.decode('utf-8'))

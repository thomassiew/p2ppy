import zmq
import time
context = zmq.Context()

# port and IP
PORT = "3d3"






#  Do 10 requests, waiting each time for a response
while True:
    socket = context.socket(zmq.REQ)
    print("Connecting to server…")
    socket.connect("tcp://localhost:5555")
    print("Sending IP + PORT")
    print("tcp://localhost:%s" % PORT )
    socket.send_string("tcp://localhost:%s" % PORT )

    #  Get the reply.
    message = socket.recv()
    print("Received : %s" %  message.decode('utf-8'))
    socket.close()
    time.sleep(10)

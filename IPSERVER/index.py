import zmq
import time
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print("listening on tcp://*5555")
ipaddress = [b'tcp://127.0.0.1:2000']
while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  Do some 'work'
    if message in ipaddress:
        print("IP in address , not adding new")
        socket.send(b",".join(ipaddress))
    else:
        print("IP not in address, adding in")
        ipaddress.append(message)
        print(ipaddress)
        socket.send(b",".join(ipaddress))
    #  Send reply back to client
    time.sleep(5)

import zmq
import time
context = zmq.Context()
publisher = context.socket(zmq.PUB)


def pubips(PORTS):
    print("pubs start")
    publisher.bind('tcp://127.0.0.1:%s' % PORTS)
    while True:
        # Allow clients to connect before sending data
        time.sleep(10)
        socket.send(b'HI from port: %s' % PORTS.encode('utf-8'))

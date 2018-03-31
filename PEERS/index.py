import zmq
import time
context = zmq.Context()
ips = [b'tcp://127.0.0.1:2000',b'tcp://localhost:3asdasd3']
# port and IP
PORT = "3asdasd3"


#  Do 10 requests, waiting each time for a response
def reqip(PORTS):
    while True:
        requester = context.socket(zmq.REQ)
        print("Connecting to IP server…")
        requester.connect("tcp://localhost:5555")
        print("Sending IP + PORT")
        print("tcp://localhost:%s" % PORTS)
        requester.send_string("tcp://localhost:%s" % PORTS)
        #  Get the reply.
        message = requester.recv()
        msg = message.decode('utf-8')
        print("Received : %s" % msg)

        if "," in msg:
            print("contains more than 1")
            ipss = msg.split(",")
            for x in ipss:
                ips.append(x)
        else:
            print(" 1 only ")
            ips.append(msg)
        requester.close()
        print (" closing connection , waiting 10 secs to find new ip")
        time.sleep(10)


def subips(PORTS):
    while True:
        subscriber = context.socket(zmq.SUB)
        subscriber.setsockopt_string(zmq.SUBSCRIBE, "")

        for x in ips:
            if x.decode('utf-8') == "tcp://localhost:%s" % PORTS:
                print ("same ip")
                break

            else:
                print("Subscribing to ", x)
                subscriber.connect(x.decode('utf-8'))
                message = subscriber.recv()
                print("Received : %s" % message.decode('utf-8'))
                subscriber.close()


                time.sleep(10)


#reqip(PORT)
subips(PORT)

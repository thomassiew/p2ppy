import zmq
import time
context = zmq.Context()

def reqips(PORTS,data):
    print ("reqip start")
    while True:
        requester = context.socket(zmq.REQ)
        #print("Connecting to IP server…")
        requester.connect("tcp://localhost:5555")
        #print("Sending IP + PORT")
        #print("tcp://localhost:%s" % PORTS)
        requester.send_string("tcp://localhost:%s" % PORTS)
        #  Get the reply.
        message = requester.recv()
        msg = message.decode('utf-8')
        print("Received IPS : %s" % msg)

        if "," in msg:
            #print("contains more than 1")
            ipss = msg.split(",")
            for x in ipss:
                data.append(x)
            else:
                #print(" 1 only ")
                data.append(msg)
                requester.close()
                print (" closing connection , waiting 10 secs to find new ip")
                time.sleep(10)

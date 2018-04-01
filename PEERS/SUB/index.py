import zmq
import time
context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.setsockopt_string(zmq.SUBSCRIBE, "")

# def subips(PORTS):
#     print ("subs start")
#     while True:
#         # if not ips:
#         # #    print( "no list , sleeping.")
#         #     time.sleep(10)
#         # else:
#             for x in ips:
#                 if x == "tcp://localhost:%s" % PORTS:
#                     print ("same ip")
#
#                 else:
#                     print("Subscribing to ", x)
#                     subscriber.connect(x)
#             break
#
#     while True:
#         message = subscriber.recv()
#         print("Received from %s: %s" % (x,message.decode('utf-8')))
#         #subscriber.close()
#         time.sleep(10)
def subips(x):
    print ("subs start")
    subscriber.connect(x)
    while True:
        message = subscriber.recv()
        print("Received from %s" % message.decode('utf-8'))

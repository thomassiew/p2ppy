import zmq
import time
from PUB.index import pubips
from SUB.index import subips
from REQIP.index import reqips
from threading import Thread

ips = []
# port and IP
PORT = "400222"
print ("This is , PORT:",PORT)

# pubips(PORT)
reqips(PORT,ips)

#
#
# try:
#     t1 = Thread(target=reqip, args=(PORT,) )
#     t2 = Thread(target=subips, args=(PORT,) )
#     t3 = Thread(target=pubips, args=(PORT,) )
#     t1.start()
#     t2.start()
#     t3.start()
# except:
#     print ("error")
# #reqip(PORT)

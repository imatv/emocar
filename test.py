# Print/Gather Data of Any State from Emotiv EPOC
# Writes to data.csv

import emokit
from emokit import emotiv
import platform
if platform.system() == "Windows":
    import socket
import gevent

if __name__ == "__main__":
    #f = open('data.csv', 'w')
    headset = emotiv.Emotiv()    
    gevent.spawn(headset.setup)
    gevent.sleep(0)
    try:
        while True:
            packet = headset.dequeue()
            #f.write(str(packet.P7[0]) + "," + str(packet.P8[0]) + "\n")
            #print packet.gyro_x, packet.gyro_y
            gevent.sleep(0)
    except KeyboardInterrupt:
        headset.close()
        #f.close()
    finally:
        headset.close()
        #f.close()
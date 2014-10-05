import emokit
from emokit import emotiv
import platform
if platform.system() == "Windows":
    import socket
import gevent
import numpy as np
import serial

if __name__ == "__main__":
    headset = emotiv.Emotiv()    
    gevent.spawn(headset.setup)
    gevent.sleep(0)
    try:
        arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        , 0, 0, 0, 0, 0, 0, 0, 0, 0
        , 0, 0, 0, 0, 0, 0, 0, 0, 0
        , 0, 0, 0, 0, 0, 0, 0, 0, 0
        , 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        ser = serial.Serial('COM3', 9600)

        while True:
            packet = headset.dequeue()
            #packet.gyro_x, packet.gyro_y
            
            arr.append(packet.P8[0])
            del arr[0]
            
            variance = np.var(arr)
            
            if (variance > 900):
                ser.write('1')
                print "ACTIVE"
            else:
                ser.write('0')
                print "INACTIVE"
            gevent.sleep(0)
    except KeyboardInterrupt:
        headset.close()
        ser.close()
    finally:
        headset.close()
        ser.close()
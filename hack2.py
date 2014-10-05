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
        SCALE_CONSTANT = 10
        arrP8 = [0]*SCALE_CONSTANT               # Might have to tweak this amount.
        #arrAF4 = [0]*SCALE_CONSTANT
        
        ser = serial.Serial('COM3', 9600)

        while True:
            packet = headset.dequeue()
            #packet.gyro_x, packet.gyro_y
            
            arrP8.append(packet.P8[0])
            del arrP8[0]
            #arrAF4.append(packet.AF4[0])
            #del arrAF4[0]
            
            varianceP8 = np.var(arrP8)
            #varianceAF4 = np.var(arrAF4)
            
            buffer = ''
            
            # Straight-line movement
           
            #if (varianceAF4 > 800):
            #    buffer += 'f'
            #    print "BACKWARD \n"
            #varianceP8 > 950
            if (varianceP8 > 1200):    # Might have to tweak this threshold.
                buffer += 'b'
                print "FORWARD \n"
            else:
                buffer += 's'
                print "STOP \n"
                
            # Directional movement (left/right)
            # correct calibrate -2 from x
                # 4 to -4 sx
                # 4 to 10 rl
                # 10+ rh
                # -4 to -10 ll
                # -10- lh 
            if (packet.gyro_x-2 < 10 and packet.gyro_x-2 > -10):
                buffer += 'sx'
                print "STILL \n"
            elif (packet.gyro_x-2 >= 10):
                buffer += 'll'
                print "RIGHT LOW \n"
            elif (packet.gyro_x-2 <= -10):
                buffer += 'rl'
                print "LEFT LOW \n"
            #elif (packet.gyro_x-2 >= 10):
            #    buffer += 'lh'
            #    print "RIGHT HIGH \n"
            #elif (packet.gyro_x-2 <= -10):
            #    buffer += 'rh'
            #    print "LEFT HIGH \n"
            else:
                print "????????!!!!!!"
            ser.write(buffer)
            gevent.sleep(0)
    except KeyboardInterrupt:
        headset.close()
        ser.close()
    finally:
        headset.close()
        ser.close()
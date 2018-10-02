#!/usr/bin/env python
#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for determining if a BrickPi3 is connected to the Raspberry Pi

#!/usr/bin/python3
from __future__ import print_function
from __future__ import division

import serial
import time

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

try:
    BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
    print("BrickPi3 connected and running")
except brickpi3.FirmwareVersionError as error:
    print(error)
except:
    print("Communication with BrickPi3 unsuccessful")

# test communication with Tetrix controller
print("Pi: set up serial port; this will *** RESET *** PRIZM board !!!!")
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
# Dakai: init serial port will re-set PRIZM board !!!!
# Dakai: need to start python code on Pi first,
#       and then press GREEN button on PRIZM !!!!
time.sleep(2) # wait for 1 second for reset PRIZM

print ("***************************************************** ")
print("Please press the GREEN button to start PRIZM board !!!!")
print ("***************************************************** ")

#send out data to PRIZM until it reply
cmd = 1
while 1:
        print ("Sending out handshaking signal ::" + str(cmd) + " to Arduino")
        ser.write(str(cmd))
        ser.flush()
        input = ser.read()
        if input == "":
            print ("Read NOTHING")
        else:
            print ("Read input ::"+ input.decode("utf-8") + " from Arduino")
            print (" ************************* ")
            print (" Get Connected to PRIZM !! ")
            print (" ************************* ")
            break  # once receive the handshake mesage, go to next loop to conrol motor          
        cmd= cmd+1
        if cmd == 5:
            cmd = 1
        time.sleep(0.01)

#send out command
cmd = 6
count = 0;
while 1:
        print ("Sending out ::"+ str(cmd) + " to Arduino")
        ser.write(str(cmd))
        ser.flush()
        input = ser.read()
        print ("Read input ::"+ input.decode("utf-8") + " from Arduino")
        count += 1;
        if(count == 10) break;


cmd = 7
while 1:
        print ("Sending out ::"+ str(cmd) + " to Arduino")
        ser.write(str(cmd))
        ser.flush()
        input = ser.read()
        print ("Read input ::"+ input.decode("utf-8") + " from Arduino")
        input += 1;
        if(input == 10) break;
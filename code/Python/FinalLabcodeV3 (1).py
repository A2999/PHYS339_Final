# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 23:06:53 2022

@author: wille
"""

#Import pySerial library
import serial
import spinmob

import numpy as np

#Import time library
import time as t
import matplotlib.pyplot as plt
data = []
Data = []
frequency = 400
frequency = int(frequency/1000*255)

#8-bit value to be written to PWB pin

#Initialize serial port and label port ’serialPort’
serialPort=serial.Serial()

#Set baud-rate to 9600
serialPort.baudrate = 115200

serialPort.port="COM6"

#Prints port specifications
#print(serialPort)

#Open serial port
serialPort.open()



dataRead=False

while (dataRead==False):
    serialPort.write(bytes([1]))
    t.sleep(0.001)
    inByte = serialPort.in_waiting
    
    while (inByte>0):
        if(len(data)>100):
            dataRead = True
            break

        #print(serialPort.readline().decode(encoding="utf-8", errors="strict"))
        data.append(serialPort.readline().decode(encoding="utf-8", errors="strict"))
        
    

serialPort.close()
           
data = data[:-1] 

for s in data:
    Data.append(float(s))  

data = np.array(Data)

plt.plot(Data, 'o')
#np.savetxt('rawData/buzz1000hz.csv', data)


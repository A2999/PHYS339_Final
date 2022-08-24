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
    serialPort.write(bytes([frequency]))
    t.sleep(0.001)
    inByte = serialPort.in_waiting
    
    while (inByte>0):
        if(len(data)>100):
            dataRead = True
            break

        #print(serialPort.readline().decode(encoding="utf-8", errors="strict"))
        data.append(serialPort.readline().decode(encoding="utf-8", errors="strict"))
        
    
serialPort.write(bytes([0]))
serialPort.close()
           
data = data[:-1] 

for s in data:
    Data.append(float(s))  

data = np.array(Data)

plt.plot(Data, 'o')
np.savetxt('rawData/buzz50hz', data)

# inputt = np.arange(0, 1500, 5)
# Data = np.delete(Data, 0)
# inputt = np.delete(inputt, 0)
# for i in range(len(Data)):
#     Data[i] = 0.97765 * Data[i] + 4.5
#Close serial port


# f1=plt.figure()
# plt.plot(inputt, Data, 'o')
# plt.xlabel("")
# plt.ylabel("")

# f = spinmob.data.fitter()

# # Set the functions
# f.set_functions('a*x+b', 'a=1, b = 0')

# # Supply the data
# f.set_data(inputt, Data, 0.01, xlabel='', ylabel='')

# # Fit!
# f.fit()
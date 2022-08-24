# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:15:07 2022

@author: weaton
"""

#Import pySerial library
import serial

#Import time library
import time as t

#8-bit value to be written to PWB pin
value=100

#Initialize serial port and label port ’serialPort’
serialPort=serial.Serial()

#Set baud-rate to 9600
serialPort.baudrate= 115200
#Set port name to that of Arduino-need to replace ? with correct COM port number
serialPort.port="COM6"
#Prints port specifications
print(serialPort)

#Open serial port
serialPort.open()

#Send write values to serial port until response character "W" is received
dataRead=False

while (dataRead==False):
    
    serialPort.write(bytes([value]))
    t.sleep(0.1)
    
    inByte = serialPort.in_waiting
    if (inByte>0):
        serialStringIn = serialPort.readline().decode(encoding="utf-8", errors="strict")
        print(serialStringIn)

serialPort.close()

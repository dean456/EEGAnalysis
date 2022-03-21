import serial
from NeuroPy import NeuroPy
from time import sleep
import os
import sys

ser = serial.Serial("COM3",9600)
ser1 = serial.Serial("COM5",9600)
#if not ser.isOpen():
#	ser.open()
#print('COM3 is open', ser.isOpen())
#print("hello:"+str(ser.read(1)))	

#neuropy = NeuroPy.NeuroPy("COM3",9600)


def attention_callback(attention_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of attention is: ", attention_value)
    return None
	
def rawValue_callback(rawValue):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("rawValue is: ", rawValue)
    return None

def blink_callback(value):
    print("Blink ", value)

#neuropy.setCallBack("attention", attention_callback)
#neuropy.setCallBack("rawValue", rawValue_callback)
#neuropy.setCallBack("blinkStrength",blink_callback)
#neuropy.start()

try:
    while True:
	    print("i'm running")
	    print("MrESP:"+str(ser.read(1).hex()))
	    print("Mindwave:"+str(ser1.read(1).hex()))
	    sleep(0.2)
finally:
    neuropy.stop()
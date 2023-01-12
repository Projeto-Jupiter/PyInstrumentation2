#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name

import serial,time



print('Running. Press CTRL-C to exit.')
with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
    time.sleep(0.1) #wait for serial to open
    if arduino.isOpen():
        print("{} connected!".format(arduino.port))
        try:
            while True:
                # cmd=input("Enter command : ")
                data_raw = arduino.readline().decode('utf-8')
                arduino.flushInput() #remove data after reading
                data_string = data_raw.replace('\r\n','').split(',')

                data_array = []
                try:
                    for element in data_string:
                        data_array.append(float(element))
                    data_array[0] = int(data_array[0])
                except: pass
                print(data_array)
                
                # print(list(data))
                #time.sleep(0.1) #wait for arduino to answer
                # while arduino.inWaiting()==0: pass
                # if  arduino.inWaiting()>0: 
                #     answer=arduino.readline()
                #     print(answer)
        except KeyboardInterrupt:
            print("KeyboardInterrupt has been caught.")
import serial,time,socket,pickle
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)           # set GPIO24 as an output   

HOST = '192.168.1.100'                 # Symbolic name meaning all available interfaces
PORT = 50005              # Arbitrary non-privileged port
serial_state = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)

        with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
            time.sleep(0.1) #wait for serial to open
            if arduino.isOpen():
                print("{} connected!".format(arduino.port))

            while not serial_state:
                try:
                    data_raw = arduino.readline().decode('utf-8')
                    arduino.flushInput() #remove data after reading
                    data_string = data_raw.replace('\r\n','').split(',')
                    serial_state = True
                except UnicodeDecodeError:
                    print('UnicodeDecodeError detected')
                    pass

                try:
                    while True:
                        data = pickle.loads(conn.recv(1024))

                        data_raw = arduino.readline().decode('utf-8')
                        arduino.flushInput() #remove data after reading
                        data_string = data_raw.replace('\r\n','').split(',')

                        data_array = []
                        try:
                            for element in data_string:
                                data_array.append(float(element))
                            data_array[0] = int(data_array[0])

                            for i in range(len(data_array)):
                                data[i] = data_array[i]
                            conn.sendall(pickle.dumps(data))

                            if data[3]:
                                GPIO.output(40,1)
                                conn.sendall(pickle.dumps(data))

                            elif not data[3]:
                                GPIO.output(40,0)
                                conn.sendall(pickle.dumps(data)) 
                        except: 
                            conn.sendall(pickle.dumps([0,0,0,0]))
                        # print(list(data))
                        #time.sleep(0.1) #wait for arduino to answer
                        # while arduino.inWaiting()==0: pass
                        # if  arduino.inWaiting()>0: 
                        #     answer=arduino.readline()
                        #     print(answer)
                except KeyboardInterrupt:
                    print("KeyboardInterrupt has been caught.")
                    GPIO.output(40,0)
                    GPIO.cleanup()
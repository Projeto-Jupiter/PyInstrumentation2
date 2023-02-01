import serial,time,socket,pickle,sys, datetime, csv
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)           # set GPIO24 as an output   
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)           # set GPIO24 as an output   


HOST = '192.168.1.30'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
serial_state = False
temp = 0

now = datetime.datetime.now()
data_name = now.strftime("raw_data_rpi_%Y_%m_%d__%H_%M_%S") # save current data and time in a variable
line_state_data = open('/home/almentacaohibrido/Desktop/Data/%s.csv'%data_name, 'w', newline='', encoding='utf-8') # creates csv file
w = csv.writer(line_state_data) # creates the variables that will write in csv

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)

        with serial.Serial("/dev/ttyACM0", 115200    , timeout=1) as arduino:
            time.sleep(0.1) #wait for serial to open
            if arduino.isOpen():
                print("{} connected!".format(arduino.port))

            while not serial_state:
                try:
                    data_raw = arduino.read(100).decode('utf-8')
                    arduino.flushInput() #remove data after reading
                    data_string = data_raw.replace('\r\n','').split(',')
                    serial_state = True
                except UnicodeDecodeError:
                    print('UnicodeDecodeError detected')
                    pass

                try:
                    while True:
                        data = pickle.loads(conn.recv(256))
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
                            # print(data)
                            if data[0] < temp:
                                print("ERRO")
                            temp = data[0]
                        
                            w.writerow(data)

                            conn.sendall(pickle.dumps(data))

                            if data[3]:
                                GPIO.output(40,1)

                            elif not data[3]:
                                GPIO.output(40,0)

                            if data[4]:
                                GPIO.output(38,1)

                            elif not data[4]:
                                GPIO.output(38,0)
                            
                            if not data[5]:
                                line_state_data.close() # close csv file
                                print("stop saving")
                            

                        except: 
                            conn.sendall(pickle.dumps([0,0,0,0,0]))
                            #pass
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
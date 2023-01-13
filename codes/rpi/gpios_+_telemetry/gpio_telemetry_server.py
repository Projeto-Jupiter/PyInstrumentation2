#Echo server program
import socket, pickle, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)           # set GPIO24 as an output   

HOST = '192.168.1.100'                 # Symbolic name meaning all available interfaces
PORT = 50010              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            try:
                data = pickle.loads(conn.recv(1024))
                if data[3]:
                    GPIO.output(40,1)
                    conn.sendall(pickle.dumps(data))

                elif not data[3]:
                    GPIO.output(40,0)
                    conn.sendall(pickle.dumps(data))                

            
            except KeyboardInterrupt:
                GPIO.output(40,0)
                GPIO.cleanup()
                print("Fim\n")
                break
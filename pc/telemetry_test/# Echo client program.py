# Echo client program
import socket
import pickle
import time

HOST = '192.168.1.100'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(pickle.dumps([1,2,3]))
   
    while True:
        data = pickle.loads(s.recv(1024))
        print('Received', data)
        time.sleep(0.001)
        s.sendall(pickle.dumps(data))
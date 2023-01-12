#Echo server program
import socket
import pickle

HOST = '192.168.1.100'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = pickle.loads(conn.recv(1024))
            for i in range(len(data)):
                data[i] += 1    
            print(data)
            if not data: break
            conn.sendall(pickle.dumps(data))

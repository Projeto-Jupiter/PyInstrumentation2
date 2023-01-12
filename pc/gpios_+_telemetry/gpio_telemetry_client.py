import socket,pickle,time

HOST = '192.168.1.100'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    a = [0,0,0,0]
    s.sendall(pickle.dumps(a))
   
    while True:
        data = pickle.loads(s.recv(1024))
        print('Received', data)
        time.sleep(0.001)
        data[3] = int(input('1 para ligado, 0 para desligado: '))
        s.sendall(pickle.dumps(data))
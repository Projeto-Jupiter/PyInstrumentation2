import time
import telnetlib

HOST = "192.168.1.100"
user = 'almentacaohibrido'
password = 'h1br1_pr0p'

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    
tn.write(b'/bin/python3 /home/almentacaohibrido/Desktop/prototipo_integrado.py\n')



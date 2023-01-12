###############cliente TCP###########

#!/usr/bin/python3
import socket
import time

IP_Servidor = '192.168.1.100'             
# Endereco IP do Servidor

PORTA_Servidor = 50007
# Porta em que o servidor estara ouvindo

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = INET (exemplo IPv4)sockets, #socket.SOCK_STREAM=usaremos TCP

DESTINO = (IP_Servidor, PORTA_Servidor) 
#destino(IP + porta)

tcp.connect(DESTINO) 

Mensagem = [1,2,3] 

# inicia a conexao TCP
try:
    while 1:
 
        # Mensagem recebera dados do teclado
        
        tcp.sendall(bytearray(Mensagem))
        # enviar a mensgem para o destinoda conexao(IP + porta)   
        #bytes(Mensagem,"utf8") = converte tipo  str para byte 
        
        print(tcp.recv(2**24))

        # Mensagem = list()

        # for i in range(len(Mensagem)):
        #     Mensagem[i] += 1

        print(Mensagem)
  

except KeyboardInterrupt:
    tcp.close()
    # finalizar o socket   
    print('fechado')                     


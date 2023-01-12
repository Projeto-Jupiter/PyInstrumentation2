import PySimpleGUI as sg
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import time
import random
from tkinter import *


# n = 20
# x=np.zeros(n)
# y=np.zeros(n)

# for i in range(n):
#     x[i] = i 
#     y[i] = random.gauss(0,400)

# ax=plt.subplot(111)

# for i in range(n):
#     ax.plot(x[0:i],y[0:i])
#     plt.savefig('fig2')
#     plt.pause(0.5)
#     time.sleep(0.2)


root = Tk()

def graph()
img = PhotoImage(file="fig2.png")

label_imagem = Label(root, image= img).pack()

root.mainloop()

# class TelaPython:
#     def __init__(self):
#         #Layout
#         botoes = [
#             [sg.Text('Válvulas:'),],
#             [sg.Button('QV1'), sg.Button('QV2'), sg.Button('QV3'),sg.Button('QV4')],
#             [sg.Output(size=(30,20),key='output')]
#         ]

#         graficos = [
#             [sg.Text('Válvulas:')]
#         ]

#         layout = [
#             [sg.Column(botoes), sg.Column(graficos)]
#         ]

#         #Janela
#         self.janela = sg.Window('Alimentação do Híbrido').layout(layout)
#         #Dados

#     def QV_change_status(qv,i):
#         qv = not qv
        
#         if qv:
#             print("QV%d ativada" %(i))
#         elif not qv:
#             print("QV%d desativada" %(i))
        
#         return int(qv)


#     def Iniciar(self):
#         while True:
#             self.button, self.values = self.janela.Read()

#             match(self.button):
#                 case 'QV1':
#                     states[1] = TelaPython.QV_change_status(states[1],1)
#                 case 'QV2':
#                     states[2] = TelaPython.QV_change_status(states[2],2)
#                 case 'QV3':
#                     states[3] = TelaPython.QV_change_status(states[3],3)
#                 case 'QV4':
#                     while True:
#                         print(datetime.now())
#                         print(states,"\n")
#                 case None:
#                     print('fechei')
#                     break
            

#             print(datetime.now())
#             print(states,"\n")
# tela = TelaPython()
# tela.Iniciar()


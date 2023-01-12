from tkinter import *
from datetime import datetime
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import time
import random
from PIL import ImageTk, Image


instant=[]
pressure=[]
temperature=[]

t0 =time.time()
states = [t0, False, False, False, 0, 0]



def QV1_button():
    states[1] = not states[1]

    if states[1]:
        print("QV1 ativada")
    elif not states[1]:
        print("QV1 desativada")

def QV2_button():
    states[2] = not states[2]

    if states[2]:
        print("QV2 ativada")
    elif not states[2]:
        print("QV2 desativada")

def QD_button():
    states[3] = not states[3]

    if states[3]:
        print("Quick Disconnect acionado")

def teste():
    t = time.time()
    states[0] = round(1*(t-t0))
    stt = str(states)
    l1.config(text=stt)
    l1.after(100,teste)

def graficos():
    instant.append(states[0])
    pressure.append(states[4])
    temperature.append(states[5])
    
    plt.figure(figsize=(4,4))
    plt.plot(instant,pressure)
    plt.savefig('fig4')

    img1 = PhotoImage(file="fig4.png")
    l2.config(image=img1)
    l2.after(1000,graficos)



app=Tk()
app.title('Alimentação do Híbrido')
app.geometry('2000x1000')
app.configure(background='#008')

l1 = Label(app, text='')
l1.place(x=10,y=100,width=200,height=70)

img = PhotoImage(file="fig2.png")
l2 = Label(app,image=img)
l2.place(x=500,y=400,width=500,height=500)



txt1=Label(app,text='Válvulas',background='#ff0',foreground='#000')
txt1.place(x=10,y=10,width=100,height=20)

qv1=Button(app,text='QV1',command=QV1_button).place(x=10,y=270)

qv2=Button(app,text='QV2',command=QV2_button).place(x=50,y=270)

qd=Button(app,text='Quick Disconnect',command=QD_button).place(x=90,y=270)

graficos()
teste()
app.mainloop()

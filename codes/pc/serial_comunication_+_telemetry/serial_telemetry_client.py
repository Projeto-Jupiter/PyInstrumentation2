import socket,pickle,time
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

def update():

    global x,y,z
    
    data = pickle.loads(s.recv(256))
    
    x = x[1:]
    x.append(data[0])
    
    y = y[1:]
    y.append(data[1])

    z = z[1:]
    z.append(data[2])
    
    data_line_1.setData(x,y)
    data_line_3.setData(x,z)

    print(data)

    s.sendall(pickle.dumps(data))

    data = pickle.loads(s.recv(1024))
    s.sendall(pickle.dumps(data))

HOST = '192.168.1.100'    # The remote host
PORT = 50008              # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(pickle.dumps([0,0,0]))
   
    # while True:
    #     data = pickle.loads(s.recv(1024))
    #     print('Received', data)
    #     s.sendall(pickle.dumps(data))
        
    #Creating GUI
    app = pg.mkQApp() #create app variable

    mw = QtWidgets.QMainWindow() #criate main window variable
    mw.setWindowTitle('Hybrid Control GUI') #set window title
    cw = QtWidgets.QWidget() #create central widget
    mw.setCentralWidget(cw) #set central widget

    #the rows below create some layouts
    l1 = QtWidgets.QVBoxLayout() 
    cw.setLayout(l1) #set layout l2 as the central widget layout

    pw1 = pg.PlotWidget(name='Plot1',title="Line Temperature Now",labels={'left': ('Temperature(K)'), 'bottom': ('Time(ms)')})  ## giving the plots names allows us to link their axes togethe
    pw3 = pg.PlotWidget(name='Plot3',title="Line Pressure Now",labels={'left': ('Pressure(bar)'), 'bottom': ('Time(ms)')})

    l1.addWidget(pw1)
    l1.addWidget(pw3)

    mw.show() #open the main window in full screen
    x = list(np.zeros(200))  # 100 time points    
    y = list(np.zeros(200))  # 100 data points
    z = list(np.zeros(200))  # 100 data points
    
    pen2 = pg.mkPen(color=(0, 255, 0))
    data_line_1 = pw1.plot(x,y,pen = pen2)
    data_line_3 =  pw3.plot(x, z, pen=pen2)



    #Set timer
    timer = QtCore.QTimer()
    timer.setInterval(50)
    timer.timeout.connect(update)
    timer.start()

    pg.exec()
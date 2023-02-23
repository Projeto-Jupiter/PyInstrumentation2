import socket,pickle
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

#Functions
def qv1():
    """Event activated by the slection of the QV1 checkbox.
    If checked, the element referent of QV1 valve satate is set as True, else, it is set as False."""
    
    global data
    
    data[3] = not data[3]

def update():

    global data
    
    data[0:3] = pickle.loads(s.recv(256))[0:3]

    s.sendall(pickle.dumps(data))


HOST = '192.168.1.100'    # The remote host
PORT = 50010              # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = [0,0,0,0]
    s.sendall(pickle.dumps(data))

    #Creating GUI
    app = pg.mkQApp() #create app variable

    mw = QtWidgets.QMainWindow() #criate main window variable
    mw.setWindowTitle('Hybrid Control GUI') #set window title
    cw = QtWidgets.QWidget() #create central widget
    mw.setCentralWidget(cw) #set central widget

    #the rows below create some layouts
    l1 = QtWidgets.QVBoxLayout() 
    cw.setLayout(l1) #set layout l2 as the central widget layout

    btn_QV1 = QtWidgets.QPushButton('Valvula')
    btn_QV1.clicked.connect(qv1) #connect qv1 button to function qv1

    l1.addWidget(btn_QV1)

    mw.show() #open the main window in full screen

    #Set timer
    timer = QtCore.QTimer()
    timer.setInterval(50)
    timer.timeout.connect(update)
    timer.start()

    pg.exec()
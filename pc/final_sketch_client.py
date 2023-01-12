import socket,pickle,time
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

#Functions
def qv1():
    """Event activated by the slection of the QV1 checkbox.
    If checked, the element referent of QV1 valve satate is set as True, else, it is set as False."""
    
    global data
    
    if btn_QV1.checkState(): #check if it is toggled
        data[3] = True #set QV1 valve state element as True if toggled
        print ('QV1 on')
    else:
        data[3] = False #set QV1 valve state element as True if not toggled
        print('QV1 off')

def update():
    global data
    
    data = pickle.loads(s.recv(1024))
    print('Received', data)
    time.sleep(0.001)
    s.sendall(pickle.dumps(data))

HOST = '192.168.1.100'    # The remote host
PORT = 50007              # The same port as used by the server
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

    btn_QV1 = QtWidgets.QCheckBox('Valvula')
    btn_QV1.clicked.connect(qv1) #connect qv1 button to function qv1

    l1.addWidget(btn_QV1)

    mw.show() #open the main window in full screen

    #Set timer
    timer = QtCore.QTimer()
    timer.setInterval(50)
    timer.timeout.connect(update)
    timer.start()

    pg.exec()

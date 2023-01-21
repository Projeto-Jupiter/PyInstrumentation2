import socket,pickle,telnetlib,time,sys,datetime,csv
import pyqtgraph as pg
import numpy as np
from pyqtgraph.Qt import QtCore, QtWidgets

def start_operation():
    global HOST, PORT, user, password, tn, s, timer
    
    # tn = telnetlib.Telnet(HOST)

    # tn.read_until(b"login: ")
    # tn.write(user.encode('ascii') + b"\n")

    # tn.read_until(b"Password: ")
    # tn.write(password.encode('ascii') + b"\n")

    # tn.write(b'/bin/python3 /home/almentacaohibrido/Desktop/solid_server_final_version.py\n')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    s.sendall(pickle.dumps(data))
    
    btn_start.setEnabled(False)
    btn_arm.setEnabled(True)
    btn_save.setEnabled(True)
    btn_finish.setEnabled(True)



    timer.start()

def arm():
    """Event activated by clicking in the Arm button.
    First, the Arm state is set as True.
    Then, all the buttons above get disabled.
    The Ignition button gets enabled.
    The QV2 button gets toggled, so the QV1 gets untoggled and the N20 is not wasted.
    The Arm button is changed to Disarm button.
    If the data is not being saved yet, is starts to being saved."""

    global btn_ignite, btn_arm, btn_QD, btn_QV1, btn_QV2, pw1, pw3, pw5, pw7, pw8, dw1, dw2, dw3, dw4, l1, l4, l5, l6, save_status

    data[3] = True #set Arm state element as True
    btn_ignite.setEnabled(True) #enable Ignition button
    btn_save.setEnabled(False) #disaable Stop Saving button
    btn_arm.setText('Disarm') #text in Arm button gets changed to 'Disarm'
    btn_arm.clicked.disconnect(arm) #arm event gets disconnected from the Disarm button variable 
    btn_arm.clicked.connect(disarm) #disarm event gets connected to the Disarm button variable   
    if save_status == False: #check if the data are already being saved
        start_save()    #if not, starts saving

def disarm():
    """Event activated by clicking in the Disarm button.
    First, the Arm state is set as False.
    Then, all the buttons above get enabled.
    The Ignition button gets disabled.
    The Disarm button is changed to Arm button."""

    global btn_ignite, btn_arm

    print('Ignitor Disarmed')
    data[3] = False #set Arm state element as False
    btn_ignite.setEnabled(False) #disable Igniton button
    btn_save.setEnabled(True) #enable Stop Saving button
    btn_arm.setText('Arm') #text in Disarm button gets changed to 'Arm'
    btn_arm.clicked.disconnect(disarm) #disarm event gets disconnected from the Arm button variable
    btn_arm.clicked.connect(arm)  #arm event gets connected to the Arm button variable


def ignite():
    """Event activated by clicking in the Ignite button.
    Actions not well defined in this mockup yet."""
    data[4] = True
    btn_save.setEnabled(True) #enable Save Data button

def start_save():
    """Event activated by clicking in the Save Data button.
    Creates a csv file named with the current data and time"""

    global now, data_name,line_state_data,w,btn_save,save_status

    now = datetime.datetime.now() #sla pq precisa disso, mas precisa
    data_name = now.strftime("%Y_%m_%d__%H_%M_%S") #save current data and time in a variable
    line_state_data = open('c:/Users/55989/OneDrive/Documentos/GitHub/PyIntrumentation2/codes/pc/Data/%s.csv'%data_name, 'w', newline='', encoding='utf-8') #creates csv file
    w = csv.writer(line_state_data) #creates the variable that will write in csv
    btn_save.setText('Stop Saving') #chnge the texte in save button to Stop Saving
    save_status = True #set save sattus as true
    btn_save.clicked.disconnect(start_save) #start_save event gets disconnected from the Stop Saving button variable
    btn_save.clicked.connect(stop)  #stop event gets connected to the Stop Saving button variable
    


def stop():
    """Event activated by clicking in the Stop Saving button.
    Closes the csv flie."""

    global now, data_name, line_state_data,w,btn_save, line_state_data,save_status
    
    save_status = False #set save satus as False
    line_state_data.close() #close csv file
    btn_save.setText('Save Data') #chnge the texte in save button to Save Data
    btn_save.clicked.disconnect(stop) #stop event gets disconnected to the Save Data button variable
    btn_save.clicked.connect(start_save)  #start_save event gets connected from the Save Data button variable


def finish_operation():
    
    global s,timer
    
    if save_status: #check if the csv still being edited
        stop()

    s.sendall(pickle.dumps([0,0,0,0,0]))   
    timer.stop()
    tn.write(b'\x03\n')

    btn_save.setEnabled(False)
    btn_finish.setEnabled(False)
    btn_shutdown.setEnabled(True)

    

def shutdown_rpi():

    global tn

    tn.write(b'sudo shutdown now\n')
    tn.write(password.encode('ascii') + b"\n")

def update():

    global x,a,b,data,s
    
    data[0:3] = pickle.loads(s.recv(1024))[0:3]
    
    x = x[1:]
    x.append(data[0])
    
    a = a[1:]
    a.append(data[1])

    b = b[1:]
    b.append(data[2])
    
    engine_data_line_1.setData(x,a)
    engine_data_line_3.setData(x,b)

    # print(data)

    s.sendall(pickle.dumps(data))
    
    # print(data)
    
    print(sys.getsizeof(_)) # gambiarra. O plot dos gráficos fica lento sem esse erro

    data[0:3] = pickle.loads(s.recv(256))[0:3]
    s.sendall(pickle.dumps(data))

now, data_name,line_state_data,w,save_status,tn,s = [0,0,0,0,False,0,0] #gambiarra
data = [0,0,0,0,0]


HOST = '192.168.1.100'    # The remote host
PORT = 50002              # The same port as used by the server


user = 'almentacaohibrido'
password = 'h1br1_pr0p'

#Creating GUI
app = pg.mkQApp() #create app variable

mw = QtWidgets.QMainWindow() #criate main window variable
mw.setWindowTitle('Hybrid Control GUI') #set window title
cw = QtWidgets.QWidget() #create central widget
mw.setCentralWidget(cw) #set central widget

#the rows below create some layouts
l1 = QtWidgets.QVBoxLayout() 
l2 = QtWidgets.QHBoxLayout()
l3 = QtWidgets.QVBoxLayout()


cw.setLayout(l2) #set layout l2 as the central widget layout

pw5 = pg.PlotWidget(name='Plot5',title="Engine Thrust Now",labels={'left': ('Thrust(N)'), 'bottom': ('Time(ms)')})
pw7 = pg.PlotWidget(name='Plot7',title="Engine Pressure Now",labels={'left': ('Pressure(bar)'), 'bottom': ('Time(ms)')})

#rows below creates some buttons
btn_start = QtWidgets.QPushButton('Start Operation')
btn_arm = QtWidgets.QPushButton('Arm')
btn_arm.setEnabled(False) #disable arm button as default
btn_ignite = QtWidgets.QPushButton('Ignite')
btn_ignite.setEnabled(False) #disable ignite button as default
btn_save = QtWidgets.QPushButton('Save Data') 
btn_save.setEnabled(False)
btn_finish = QtWidgets.QPushButton('Finish Operation')
btn_finish.setEnabled(False)
btn_shutdown = QtWidgets.QPushButton('Shutdown RPi')
btn_shutdown.setEnabled(False)


#rows below associate events to buttons
btn_start.clicked.connect(start_operation)
btn_arm.clicked.connect(arm) #connect arm button to function arm
btn_ignite.clicked.connect(ignite) #connect ignite button to function ignite
btn_save.clicked.connect(start_save) #connect save button to function start_save
btn_finish.clicked.connect(finish_operation)
btn_shutdown.clicked.connect(shutdown_rpi)

l3.addWidget(btn_start)
l3.addWidget(btn_arm)
l3.addWidget(btn_ignite)
l3.addWidget(btn_save)
l3.addWidget(btn_finish)
l3.addWidget(btn_shutdown)

l1.addWidget(pw5)
l1.addWidget(pw7)

#rows below organize the layouts
l2.addLayout(l3)
l2.addLayout(l1)


mw.showMaximized() #open the main window in full screen

x = list(np.zeros(200))  # 100 time points    
a = list(np.zeros(200))  # 100 data points
b = list(np.zeros(200))  # 100 data points

pen1 = pg.mkPen(color=(255, 255, 0))
pen2 = pg.mkPen(color=(255, 255, 255))

engine_data_line_1 = pw5.plot(x,a,pen = pen2)
engine_data_line_3 =  pw7.plot(x,b, pen=pen1)

#Set timer
timer = QtCore.QTimer()
timer.setInterval(50)
timer.timeout.connect(update)

pg.exec()

# if save_status: #check if the csv still being edited
# save_status = not save_status #the save_status get changed
# line_state_data.close() #close the csv file
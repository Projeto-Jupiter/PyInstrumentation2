import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
import time
import datetime
import csv

#Functions
def qv1(toggled):
    """Event activated by the slection of the QV1 toggle.
    If toggled, the element referent of QV1 valve satate is set as True, else, it is set as False."""
    
    global line_state
    
    if toggled: #check if it is toggled
        line_state[3] = True #set QV1 valve state element as True if toggled
        print ('QV1 on')
    else:
        line_state[3] = False #set QV1 valve state element as True if not toggled
        print('QV1 off')

def qv2(toggled):
    """Event activated by the slection of the QV2 toggle.
    If toggled, the element referent of QV2 valve satate is set as True, else, it is set as False."""

    global line_state
    
    if toggled: #check if it is toggled
        line_state[4] = True #set QV2 valve state element as True if toggled
        print ('QV2 on')
    else:
        line_state[4] = False #set QV2 valve state element as True if not toggled
        print('QV2 off')

def qd():
    """Event activated by clicking in the Quick Disconnect (QD) button.
    First, the Quick Disconnect State is set as True.
    Then, the QV2 button gets toggled, so the QV1 gets untoggled and the N20 is not wasted.
    Finally, the Arm button gets enabled. """

    global btn_QV1, btn_QV2

    print('Quick Disconnect Activated')
    line_state[5] = True #set QD state element as True
    btn_QV2.setChecked(True) #toggle QV2 button
    btn_arm.setEnabled(True) #enable Arm button

def arm():
    """Event activated by clicking in the Arm button.
    First, the Arm state is set as True.
    Then, all the buttons above get disabled.
    The Ignition button gets enabled.
    The QV2 button gets toggled, so the QV1 gets untoggled and the N20 is not wasted.
    The Arm button is changed to Disarm button.
    If the data is not being saved yet, is starts to being saved."""

    global btn_ignite, btn_arm, btn_QD, btn_QV1, btn_QV2, pw1, pw2, pw3, pw4, pw5, pw6, pw7, pw8, dw1, dw2, dw3, dw4, l1, l4, l5, l6

    print('Ignitor Armed')
    line_state[6] = True #set Arm state element as True
    btn_QV1.setEnabled(False) #disable QV1 button
    btn_QV2.setEnabled(False) #disable QV2 button
    btn_QD.setEnabled(False) #disable QD button
    btn_ignite.setEnabled(True) #enable Ignition button
    btn_save.setEnabled(False) #disaable Stop Saving button
    btn_QV2.setChecked(True) #toggle QV2 button
    btn_arm.setText('Disarm') #text in Arm button gets changed to 'Disarm'
    btn_arm.clicked.disconnect(arm) #arm event gets disconnected from the Disarm button variable 
    btn_arm.clicked.connect(disarm) #disarm event gets connected to the Disarm button variable   
    if not save_status: #check if the data are already being saved
        start_save()    #if not, starts saving

def disarm():
    """Event activated by clicking in the Disarm button.
    First, the Arm state is set as False.
    Then, all the buttons above get enabled.
    The Ignition button gets disabled.
    The Disarm button is changed to Arm button."""

    global btn_ignite, btn_arm, btn_QD

    print('Ignitor Disarmed')
    line_state[6] = False #set Arm state element as False
    btn_QV1.setEnabled(True) #enable QV1 button
    btn_QV2.setEnabled(True) #enable QV2 button
    btn_QD.setEnabled(True)  #enable QD button
    btn_ignite.setEnabled(False) #disable Igniton button
    btn_save.setEnabled(True) #enable Stop Saving button
    btn_arm.setText('Arm') #text in Disarm button gets changed to 'Arm'
    btn_arm.clicked.disconnect(disarm) #disarm event gets disconnected from the Arm button variable
    btn_arm.clicked.connect(arm)  #arm event gets connected to the Arm button variable


def ignite():
    """Event activated by clicking in the Ignite button.
    Actions not well defined in this mockup yet."""
    print('Kambum!')
    btn_save.setEnabled(True) #enable Save Data button

def start_save():
    """Event activated by clicking in the Save Data button.
    Creates a csv file named with the current data and time"""

    global now, data_name,line_state_data,w,btn_save,save_status

    now = datetime.datetime.now() #sla pq precisa disso, mas precisa
    data_name = now.strftime("%Y_%m_%d__%H_%M_%S") #save current data and time in a variable
    line_state_data = open('Data/%s.csv'%data_name, 'w', newline='', encoding='utf-8') #creates csv file
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

def update():
    global x, y, x1, y1, z, z1, k, a, k1, a1, b, b1, line_state
    
    t = 1000*(time.time() - t0)
    x1 = x1[1:]  # Remove the first y element.
    x1.append(round(t))  # Add a new value 1 higher than the last.
    x.append(round(t))  # Add a new value 1 higher than the last.

    y1 = y1[1:]  # Remove the first
    y1.append( randint(0,100))  # Add a new random value.
    y.append( randint(0,100))  # Add a new random value.

    z1 = z1[1:]  # Remove the first
    z1.append( randint(0,100))  # Add a new random value.
    z.append( randint(0,100))  # Add a new random value.

    data_line.setData(x, y)  # Update the data.
    data_line_1.setData(x1,y1)
    data_line_2.setData(x, z)  # Update the data.
    data_line_3.setData(x1,z1)

    dw1.setText('Temperature in Line Now: %s'%line_state[1])
    dw2.setText('Pressure in Line Now: %s'%line_state[2])

    line_state[0] = t
    line_state[1] = y[len(y)-1]
    line_state[2] = z[len(z)-1]

    k1 = k1[1:]  # Remove the first y element.
    k1.append(round(t))  # Add a new value 1 higher than the last.
    k.append(round(t))  # Add a new value 1 higher than the last.

    a1 = a1[1:]  # Remove the first
    a1.append( randint(0,100))  # Add a new random value.
    a.append( randint(0,100))  # Add a new random value.

    b1 = b1[1:]  # Remove the first
    b1.append( randint(0,100))  # Add a new random value.
    b.append( randint(0,100))  # Add a new random value.

    engine_data_line.setData(k, a)  # Update the data.
    engine_data_line_1.setData(k1,a1)
    engine_data_line_2.setData(k, b)  # Update the data.
    engine_data_line_3.setData(k1,b1)

    if save_status:
        w.writerow(line_state)



#Def important parameters
now, data_name,line_state_data,w,save_status = [0,0,0,0,0] #gambiarra

line_state = [0,0,0,0,0,0,0]    #[time, temperature, pressure, qv1, qv2, quickdisconnect, arm]
motor_state = [0,0,0]   #[time, thrust, pressure]

t0 =time.time() #salva o instante em que o programa iniciou

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
l4 = QtWidgets.QVBoxLayout()
l5 = QtWidgets.QHBoxLayout()
l6 = QtWidgets.QHBoxLayout()
l7 = QtWidgets.QVBoxLayout()
l8 = QtWidgets.QVBoxLayout()



cw.setLayout(l2) #set layout l2 as the central widget layout

#rows below creates some graphics widgets
pw1 = pg.PlotWidget(name='Plot1',title="Line Temperature Now",labels={'left': ('Temperature(K)'), 'bottom': ('Time(ms)')})  ## giving the plots names allows us to link their axes togethe
pw2 = pg.PlotWidget(name='Plot2',title="Line Temperature Throughout Operation",labels={'left': ('Temperature(K)'), 'bottom': ('Time(ms)')})
pw3 = pg.PlotWidget(name='Plot3',title="Line Pressure Now",labels={'left': ('Pressure(bar)'), 'bottom': ('Time(ms)')})
pw4 = pg.PlotWidget(name='Plot4',title="Line Pressure Throughout Operation",labels={'left': ('Pressure(bar)'), 'bottom': ('Time(ms)')})
pw5 = pg.PlotWidget(name='Plot5',title="Engine Thrust Now",labels={'left': ('Thrust(N)'), 'bottom': ('Time(ms)')})
pw6 = pg.PlotWidget(name='Plot6',title="Engine Thrust Throughout Operation",labels={'left': ('Thrust(N)'), 'bottom': ('Time(ms)')})
pw7 = pg.PlotWidget(name='Plot7',title="Engine Pressure Now",labels={'left': ('Pressure(bar)'), 'bottom': ('Time(ms)')})
pw8 = pg.PlotWidget(name='Plot8',title="Engine Pressure Throughout Operation",labels={'left': ('Pressure(bar)'), 'bottom': ('Time(ms)')})


#rows below creates some buttons
btn_QV1 = QtWidgets.QRadioButton('QV1')
btn_QV2 = QtWidgets.QRadioButton('QV2')
btn_QD = QtWidgets.QPushButton('Quick Disconnect')
btn_arm = QtWidgets.QPushButton('Arm')
btn_arm.setEnabled(False) #disable arm button as default
btn_ignite = QtWidgets.QPushButton('Ignite')
btn_ignite.setEnabled(False) #disable ignite button as default
btn_save = QtWidgets.QPushButton('Save Data')

#rows below associate events to buttons
btn_QV1.toggled.connect(qv1) #connect qv1 button to function qv1
btn_QV2.toggled.connect(qv2) #connect qv2 button to function qv2
btn_QD.clicked.connect(qd) #connect quickdisconnect button to function qd
btn_arm.clicked.connect(arm) #connect arm button to function arm
btn_ignite.clicked.connect(ignite) #connect ignite button to function ignite
btn_save.clicked.connect(start_save) #connect save button to function start_save

#rows below create some label widgets
dw1 = QtWidgets.QLabel('Temperature in Line Now: %s K'%line_state[1])
dw2 = QtWidgets.QLabel('Pressure in Line Now: %s bar'%line_state[2])
dw3 = QtWidgets.QLabel('MaximumTemperature Acecptable in Line : 350 K')
dw4 = QtWidgets.QLabel('Maximum Pressure Acecptable in Line: 60 bar') 

#rows below add the widgets to the respective layouts
l5.addWidget(dw1)
l5.addWidget(dw3)

l6.addWidget(dw2)
l6.addWidget(dw4)


l3.addWidget(btn_QV1)
l3.addWidget(btn_QV2)
l3.addWidget(btn_QD)
l3.addWidget(btn_arm)
l3.addWidget(btn_ignite)
l3.addWidget(btn_save)

l4.addWidget(pw3)
l4.addWidget(pw7)

l1.addWidget(pw1)
l1.addWidget(pw5)

#rows below organize the layouts
l1.addLayout(l5)
l4.addLayout(l6)
l2.addLayout(l3)
l2.addLayout(l1)
l2.addLayout(l4)


mw.showMaximized() #open the main window in full screen

## Create plot curves
x = list(np.zeros(200))  # 100 time points
x1=x
y = list(np.zeros(200))  # 100 data points
y1=y
z = list(np.zeros(200))  # 100 data points
z1=z
a = list(np.zeros(200))  # 100 data points
a1=a
b = list(np.zeros(200))  # 100 data points
b1=b
k = list(np.zeros(200))  # 100 time points
k1=k


pen1 = pg.mkPen(color=(255, 0, 0))
pen2 = pg.mkPen(color=(0, 255, 0))
pen3 = pg.mkPen(color=(0, 0, 255))
pen4 = pg.mkPen(color=(255, 255, 0))

data_line =  pw2.plot(x, y, pen=pen2)
data_line_1 = pw1.plot(x1,y1,pen = pen2)
data_line_3 =  pw3.plot(x, z, pen=pen2)
data_line_2 = pw4.plot(x1,z1,pen = pen2)

engine_data_line =  pw6.plot(k, a, pen=pen3)
engine_data_line_1 = pw5.plot(k1,a1,pen = pen1)
engine_data_line_3 =  pw7.plot(k, b, pen=pen1)
engine_data_line_2 = pw8.plot(k1,b1,pen = pen4)

#Set timer
timer = QtCore.QTimer()
timer.setInterval(50)
timer.timeout.connect(update)
timer.start()


pg.exec()

if save_status: #check if the csv still being edited
    save_status = not save_status #the save_status get changed
    line_state_data.close() #close the csv file
    

#import modules
import sys, ast, csv, json, os
import numpy as np
from scipy import signal, integrate
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QCheckBox,
    QStackedLayout,
    QVBoxLayout,
    QTabWidget,
    QGridLayout,
    QWidget,
    QLineEdit,
    QComboBox,
    QFileDialog,
    QDialog,
    QMessageBox,
    QToolBar, 
    QAction, 
    QStatusBar,
    QShortcut,
    QInputDialog
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow, MplCanvas):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Static Fire Test Analysis")
        self.setMinimumSize(800, 600)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        # create the main widget and the layout
        self.mainWidget = QWidget(self)
        self.mainLayout = QVBoxLayout(self.mainWidget)

        # create the menu bar
        self.createMenuBar()

        # set the main widget as the central widget of the window
        self.setCentralWidget(self.mainWidget)

        # create the the plot with mplcanvas
        self.mplCanvas = MplCanvas(self.mainWidget, width=5, height=10, dpi=100)
        
        # create a grid layout to display the information
        self.gridLayout = QGridLayout()

        # create the labels and values for the information
        self.max_thrust_label = QLabel("Maximum Thrust: ")
        self.max_thrust_label.setStyleSheet("font: 12pt;")
        self.max_thrust_value = QLabel("-")
        self.max_thrust_value.setStyleSheet("font: 12pt;")
        self.max_pressure_label = QLabel("Maximum Pressure: ")
        self.max_pressure_label.setStyleSheet("font: 12pt;")
        self.max_pressure_value = QLabel("-")
        self.max_pressure_value.setStyleSheet("font: 12pt;")
        self.average_thrust_label = QLabel("Average Thrust: ")
        self.average_thrust_label.setStyleSheet("font: 12pt;")
        self.average_thrust_value = QLabel("-")
        self.average_thrust_value.setStyleSheet("font: 12pt;")
        self.average_pressure_label = QLabel("Average Pressure: ")
        self.average_pressure_label.setStyleSheet("font: 12pt;")
        self.average_pressure_value = QLabel("-")
        self.average_pressure_value.setStyleSheet("font: 12pt;")
        self.total_impulse_label = QLabel("Total Impulse: ")
        self.total_impulse_label.setStyleSheet("font: 12pt;")
        self.total_impulse_value = QLabel("-")
        self.total_impulse_value.setStyleSheet("font: 12pt;")
        self.burnout_time_label = QLabel("Burnout Time: ")
        self.burnout_time_label.setStyleSheet("font: 12pt;")
        self.burnout_time_value = QLabel("-")
        self.burnout_time_value.setStyleSheet("font: 12pt;")
        self.ISP_label = QLabel("ISP: ")
        self.ISP_label.setStyleSheet("font: 12pt;")
        self.ISP_value = QLabel("-")
        self.ISP_value.setStyleSheet("font: 12pt;")
        self.propellant_mass_label = QLabel("Propellant Mass: ")
        self.propellant_mass_label.setStyleSheet("font: 12pt;")
        self.propellant_mass_value = QLabel("-")
        self.propellant_mass_value.setStyleSheet("font: 12pt;")



        # add the labels to the grid layout in 8 columns and 2 rows with the labels aligned to the right and the values aligned to the left
        self.gridLayout.addWidget(self.max_thrust_label, 0, 0, Qt.AlignRight)
        self.gridLayout.addWidget(self.max_thrust_value, 0, 1, Qt.AlignLeft)
        self.gridLayout.addWidget(self.max_pressure_label, 1, 0, Qt.AlignRight)
        self.gridLayout.addWidget(self.max_pressure_value, 1, 1, Qt.AlignLeft)
        self.gridLayout.addWidget(self.average_thrust_label, 0, 2, Qt.AlignRight)
        self.gridLayout.addWidget(self.average_thrust_value, 0, 3, Qt.AlignLeft)
        self.gridLayout.addWidget(self.average_pressure_label, 1, 2, Qt.AlignRight)
        self.gridLayout.addWidget(self.average_pressure_value, 1, 3, Qt.AlignLeft)
        self.gridLayout.addWidget(self.total_impulse_label, 0, 4, Qt.AlignRight)
        self.gridLayout.addWidget(self.total_impulse_value, 0, 5, Qt.AlignLeft)
        self.gridLayout.addWidget(self.burnout_time_label, 1, 4, Qt.AlignRight)
        self.gridLayout.addWidget(self.burnout_time_value, 1, 5, Qt.AlignLeft)
        self.gridLayout.addWidget(self.ISP_label, 0, 6, Qt.AlignRight)
        self.gridLayout.addWidget(self.ISP_value, 0, 7, Qt.AlignLeft)
        self.gridLayout.addWidget(self.propellant_mass_label, 1, 6, Qt.AlignRight)
        self.gridLayout.addWidget(self.propellant_mass_value, 1, 7, Qt.AlignLeft)

        #set disatnce between the rows
        self.gridLayout.setRowMinimumHeight(0, 80)
        self.gridLayout.setRowMinimumHeight(1, 80)





        



        # add the mplcanvas and the grid layout to the main layout
        self.mainLayout.addWidget(self.mplCanvas)
        self.mainLayout.addLayout(self.gridLayout)

        # set the main widget as the central widget of the window
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

    def createMenuBar(self):
        menu = self.menuBar()

        # create the file menu
        fileMenu = menu.addMenu("File")

        # create the file menu actions
        openAction = QAction("Open Raw", self)
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        # saveAction = QAction("Save", self)
        # saveAction.setShortcut("Ctrl+S")
        # saveAction.triggered.connect(self.saveFile)
        # fileMenu.addAction(saveAction)

        # saveAsAction = QAction("Save As", self)
        # saveAsAction.setShortcut("Ctrl+Shift+S")
        # saveAsAction.triggered.connect(self.saveAsFile)
        # fileMenu.addAction(saveAsAction)

        exitAction = QAction("Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(self.exitApp)
        fileMenu.addAction(exitAction)

        # create the export menu
        self.exportMenu = menu.addMenu("Export")
        self.exportMenu.setEnabled(False)
        
        # create the export menu actions
        exportThrustAction = QAction("Thrust", self)
        exportThrustAction.triggered.connect(self.exportThrustcsv)
        self.exportMenu.addAction(exportThrustAction)    

        exportPressureAction = QAction("Pressure", self)
        exportPressureAction.triggered.connect(self.exportPressurecsv)
        self.exportMenu.addAction(exportPressureAction)

        exportAllAction = QAction("All", self)
        exportAllAction.triggered.connect(self.exportAllcsv)
        self.exportMenu.addAction(exportAllAction)

        exportWindowAction = QAction("Window", self)
        exportWindowAction.triggered.connect(self.exportWindowpng)
        self.exportMenu.addAction(exportWindowAction)

        # create the help menu
        helpMenu = menu.addMenu("Help")

        # create the help menu actions
        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(self.aboutApp)
        helpMenu.addAction(aboutAction)

        # create the status bar 
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def openFile(self):
        self.exportMenu.setEnabled(True)

        # open a file dialog and get the selected file
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", os.getcwd(), "CSV Files (*.csv)")
        if fileName:
            # open the file and read the data
            with open(fileName, 'r') as file:
                reader = csv.reader(file)
                self.data = list(reader)

        #open dialog window to receive user input for the propellant mass
        self.propellant_mass, ok = QInputDialog.getDouble(self, "Propellant Mass", "Enter the propellant mass in grams:", 2000, 0, 100000, 0)

        if ok:
            self.propellant_mass = self.propellant_mass/1000
        #set the propellant mass qinputdialog size



        #define data arrays
        self.time = []
        self.thrust = []
        self.pressure = []

        #read data from csv file
        for i in range(len(self.data)):
            self.time.append(float(self.data[i][0]))
            self.thrust.append(float(self.data[i][1]))
            self.pressure.append(float(self.data[i][2]))

        #convert time to seconds
        self.time = np.array(self.time)
        self.time = self.time/1000

        #creates arrays of time, thrust and pressure values which correspond to the thrust values greater than 15
        self.burn_time = []
        self.burn_thrust = []
        self.burn_pressure = []
        for i in range(len(self.thrust)):
            if self.thrust[i] > 20:
                self.burn_time.append(self.time[i])
                self.burn_thrust.append(self.thrust[i])
                self.burn_pressure.append(self.pressure[i])

        #filter the arrays to remove time, thrust and pressure values which correspond to instants which the time is lower than the previous instant
        self.time_filtered = []
        self.thrust_filtered = []
        self.pressure_filtered = []
        for i in range(len(self.burn_time)):
            if i == 0:
                self.time_filtered.append(self.burn_time[i])
                self.thrust_filtered.append(self.burn_thrust[i])
                self.pressure_filtered.append(self.burn_pressure[i])
            else:
                if self.burn_time[i] > self.burn_time[i-1]:
                    self.time_filtered.append(self.burn_time[i])
                    self.thrust_filtered.append(self.burn_thrust[i])
                    self.pressure_filtered.append(self.burn_pressure[i])

        #make the time filtered array start at 0
        self.time_filtered = np.array(self.time_filtered)
        self.time_filtered = self.time_filtered - self.time_filtered[0]

        #smooth the filtered thrust and pressure data
        self.thrust_filtered = signal.savgol_filter(self.thrust_filtered, 51, 3)
        self.pressure_filtered = signal.savgol_filter(self.pressure_filtered, 51, 3)

        #plot the filtered thrust and pressure data in the same mplcanvas with two different y axes
        self.mplCanvas.axes.clear()
        #add a title to the plot
        self.mplCanvas.axes.set_title('Thrust and Pressure vs Time')
        self.mplCanvas.axes.plot(self.time_filtered, self.thrust_filtered, color = 'red')
        self.mplCanvas.axes.set_xlabel('Time (s)')
        self.mplCanvas.axes.set_ylabel('Thrust (N)', color = 'red')
        self.mplCanvas.axes.tick_params(axis = 'y', labelcolor = 'red')
        self.mplCanvas.axes2 = self.mplCanvas.axes.twinx()
        self.mplCanvas.axes2.plot(self.time_filtered, self.pressure_filtered, color = 'blue')
        self.mplCanvas.axes2.set_ylabel('Pressure (bar)', color = 'blue')
        self.mplCanvas.axes2.tick_params(axis = 'y', labelcolor = 'blue')
        #add a grid to the plot
        self.mplCanvas.axes.grid()
        #redraw the plot
        self.mplCanvas.draw()

        #get the maximuns of the thrust and pressure data
        self.thrust_max = max(self.thrust_filtered)
        self.pressure_max = max(self.pressure_filtered)

        #get the average thrust and pressure
        self.thrust_avg = np.mean(self.thrust_filtered)
        self.pressure_avg = np.mean(self.pressure_filtered)

        #evaulate the total impulse value by integrating the filtered thrust data
        self.total_impulse = integrate.simps(self.thrust_filtered, self.time_filtered)

        #evaluate isp by dividing the total impulse by the propellant weight
        self.isp = self.total_impulse/(self.propellant_mass*9.81)

        #update values QLabels with the calculated values
        self.max_thrust_value.setText('{:.0f}N at {:.2f}s'.format(self.thrust_max, self.time_filtered[np.argmax(self.thrust_filtered)]))
        self.max_pressure_value.setText('{:.2f}bar at {:.2f}s'.format(self.pressure_max, self.time_filtered[np.argmax(self.pressure_filtered)]))
        self.average_thrust_value.setText('{:.0f}N'.format(self.thrust_avg))
        self.average_pressure_value.setText('{:.2f}bar'.format(self.pressure_avg))
        self.total_impulse_value.setText('{:.0f}Ns'.format(self.total_impulse))
        self.burnout_time_value.setText('{:.2f}s'.format(self.time_filtered[-1]))
        self.ISP_value.setText('{:.0f}s'.format(self.isp))
        self.propellant_mass_value.setText('{:.2f}kg'.format(self.propellant_mass))


        # update the status bar
        self.statusBar.showMessage('Opened file: ' + fileName)

    def saveFile(self):
        # open a file dialog and get the selected file
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", os.getcwd(), "CSV Files (*.csv)")
        if fileName:
            # open the file and write the data
            with open(fileName, 'w') as file:
                writer = csv.writer(file)
                writer.writerows(self.data)

            # update the status bar
            self.statusBar.showMessage('Saved file: ' + fileName)

    def saveAsFile(self):
        # open a file dialog and get the selected file
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File As", os.getcwd(), "CSV Files (*.csv)")
        if fileName:
            # open the file and write the data
            with open(fileName, 'w') as file:
                writer = csv.writer(file)
                writer.writerows(self.data)

            # update the status bar
            self.statusBar.showMessage('Saved file as: ' + fileName)

    def exitApp(self):
        # exit the application
        sys.exit()

    def exportThrustcsv(self):
        # open a file dialog and get the selected file
        fileName, _ = QFileDialog.getSaveFileName(self, "Export Thrust CSV", os.getcwd(), "CSV Files (*.csv)")
        if fileName:
            # open the file and write the data
            with open(fileName, 'w') as file:
                writer = csv.writer(file)
                writer.writerows([self.time_filtered, self.thrust_filtered])

            # update the status bar
            self.statusBar.showMessage('Exported Thrust CSV: ' + fileName)
    
    def exportPressurecsv(self):
        # open a file dialog and get the selected file
        fileName, _ = QFileDialog.getSaveFileName(self, "Export Pressure CSV", os.getcwd(), "CSV Files (*.csv)")
        if fileName:
            # open the file and write the data
            with open(fileName, 'w') as file:
                writer = csv.writer(file)
                writer.writerows([self.time_filtered, self.pressure_filtered])

            # update the status bar
            self.statusBar.showMessage('Exported Pressure CSV: ' + fileName)

    def exportAllcsv(self):
        # open a file dialog and get the selected file
        fileName, _ = QFileDialog.getSaveFileName(self, "Export All CSV", os.getcwd(), "CSV Files (*.csv)")
        if fileName:
            # open the file and write the data
            with open(fileName, 'w') as file:
                writer = csv.writer(file)
                writer.writerows([self.time_filtered, self.thrust_filtered, self.pressure_filtered])

            # update the status bar
            self.statusBar.showMessage('Exported All CSV: ' + fileName)

    def exportWindowpng(self):
        # open a file dialog and get the selected file
        fileName, _ = QFileDialog.getSaveFileName(self, "Export Window PNG", os.getcwd(), "PNG Files (*.png)")
        if fileName:
            # open the file and write the data
            self.mplCanvas.figure.savefig(fileName)

            # update the status bar
            self.statusBar.showMessage('Exported Window PNG: ' + fileName)

    def aboutApp(self):
        # create a message box
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("About")
        msgBox.setText("Static Fire Test Analysis")
        msgBox.setInformativeText("Version 1.0.0")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
        msgBox.show()

    def helpApp(self):
        # create a message box
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Help")
        msgBox.setText("Static Fire Test Analysis")
        msgBox.setInformativeText("Help")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
        msgBox.show()









if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())



    

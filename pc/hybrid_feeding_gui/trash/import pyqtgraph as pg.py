from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QHBoxLayout,
    QWidget,
    QVBoxLayout
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Widgets App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QVBoxLayout()

        widgets1 = [
            QCheckBox,

        ]

        widgets2 = [
            QPushButton('QV1'),
            QCheckBox('QV2'),
            QCheckBox('Quick Disconnect'),

        ]

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        widgets2[0].clicked.connect(self.show_state_QV1)
        widgets2[1].stateChanged.connect(self.show_state_QV2)
        widgets2[2].stateChanged.connect(self.show_state_Quick_Disconnect)        
        widgets3 = [
            QCheckBox,

        ]


        for w in widgets2:
            layout2.addWidget(w)

        layout1.addLayout( layout2 )

        for w in widgets1:
             layout4.addWidget(w('B'))

        for w in widgets3:
            layout3.addWidget(w('C'))

        # self.graphWidget = pg.PlotWidget()

        # self.x = list(range(100))  # 100 time points
        # self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        # self.graphWidget.setBackground('w')

        # pen = pg.mkPen(color=(255, 0, 0))
        # self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)

        # layout3.addWidget(self.graphWidget)

        layout5.addLayout( layout3 )
        layout5.addLayout( layout4 )
        
        layout1.addLayout( layout5 )

        widget = QWidget()
        widget.setLayout(layout1)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


    
    def show_state_QV1(self, s):
        print('QV1: ',s == Qt.Checked)

    def show_state_QV2(self, s):
        print('QV2: ',s == Qt.Checked)

    def show_state_Quick_Disconnect(self, s):
        print('Quick Disconnect: ',s == Qt.Checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

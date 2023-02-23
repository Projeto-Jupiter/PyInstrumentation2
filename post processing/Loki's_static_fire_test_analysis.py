#import modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import os
import sys
import math
import scipy
from scipy import signal
from scipy import stats
from scipy import interpolate
from scipy import integrate
from scipy import optimize
from scipy import special
from scipy import linalg
from scipy import fftpack
from scipy import spatial


# import data from data folder
# Path: .\data\
# File: Loki_static_fire_test_6s.csv
data = pd.read_csv('.\data\Loki_static_fire_test.csv', sep=',', header=0)
data = data.dropna(axis=1, how='all')
data = data.dropna(axis=0, how='all')
data = data.dropna(axis=0, how='any')
data = data.reset_index(drop=True)

# define data arrays
# data first column is time in ms
# data second column is thrust in N
# data third column is pressure in bar

time = data.iloc[:,0]
thrust = data.iloc[:,1]
pressure = data.iloc[:,2]

# convert time to seconds
time = time/1000


# create a time array with just the time wich the trhust is above 15 N
time_start = time[thrust > 15].iloc[0]
time_end = time[thrust > 15].iloc[-1]
time_burn = time[(time > time_start) & (time < time_end)]
# make time_burn start at 0
time_burn = time_burn - time_burn.iloc[0]

# creat thrust curve between start and end of burn
thrust_curve = thrust[(time > time_start) & (time < time_end)]
#create pressure curve between start and end of burn
pressure_curve = pressure[(time > time_start) & (time < time_end)]

# smooth the thrust curve
thrust_curve = signal.savgol_filter(thrust_curve, 51, 3)

# smooth the pressure curve
pressure_curve = signal.savgol_filter(pressure_curve, 51, 3)

# find the maximum thrust
max_thrust = thrust_curve.max()

# find the maximum pressure
max_pressure = pressure_curve.max()

# find the time of maximum thrust
max_thrust_time = time[(time > time_start) & (time < time_end)][thrust_curve == max_thrust].iloc[0] - time_start

# find the time of maximum pressure
max_pressure_time = time[(time > time_start) & (time < time_end)][pressure_curve == max_pressure].iloc[0] - time_start

# find the average thrust
avg_thrust = thrust_curve.mean()

# find the average pressure
avg_pressure = pressure_curve.mean()

# find the burn time
burn_time = time_end - time_start

# find the total impulse
total_impulse = integrate.trapz(thrust_curve, time[(time > time_start) & (time < time_end)])

# find the isp
propellant_weight = 1.409*9.81 #N
isp = total_impulse/propellant_weight

# plot both curves in the same figure with different y axes
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('thrust (N)', color=color)
ax1.plot(time_burn, thrust_curve, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid()

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('pressure (bar)', color=color)  # we already handled the x-label with ax1
ax2.plot(time_burn, pressure_curve, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title("Loki's thrust and pressure curves")

# print results
print('Maximum thrust: ' + str(max_thrust) + ' N at ' + str(max_thrust_time) + ' s')
print('Maximum pressure: ' + str(max_pressure) + ' bar at ' + str(max_pressure_time) + ' s')
print('Average thrust: ' + str(avg_thrust) + ' N')
print('Average pressure: ' + str(avg_pressure) + ' bar')
print('Burn time: ' + str(burn_time) + ' s')
print('Total impulse: ' + str(total_impulse) + ' Ns')
print('Isp: ' + str(isp) + ' s')

# put the results printed in the plot window in the right side of the plot and organize them in a table
results = 'Maximum thrust: ' + str(max_thrust) + ' N at ' + str(max_thrust_time) + ' s \n' + 'Maximum pressure: ' + str(max_pressure) + ' bar at ' + str(max_pressure_time) + ' s \n' + 'Average thrust: ' + str(avg_thrust) + ' N \n' + 'Average pressure: ' + str(avg_pressure) + ' bar \n' + 'Burn time: ' + str(burn_time) + ' s \n' + 'Total impulse: ' + str(total_impulse) + ' Ns \n' + 'Isp: ' + str(isp) + ' s'
plt.figtext(0.7, 0.5, results, wrap=True, horizontalalignment='left', fontsize=12)

#organize plot window
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.6, top=0.9, wspace=0.2, hspace=0.2)

# show the plot
plt.show()












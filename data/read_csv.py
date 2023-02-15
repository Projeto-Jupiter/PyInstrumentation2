# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

# Initialize arrays for x and y
x = [0]
y = [0]

# Open the data file
dataset = open('C:\\Users\\eduar\\OneDrive\\Documents\\GitHub\\PyInstrumentation2\\data\\Loki_static_fire_test.csv', 'r')

# Define minimum and maximum values for x
min = float(175500)
max = float(182000)

# Loop through the data file
for line in dataset:
    line = line.strip("\n")
    # X is the first column, Y is the second column
    X,Y,A,B,C,D = line.split(',') # gambiarra
    # Check if X is greater than the last value in x
    if int(X) > x[len(x)-1]:
        # Check if X is within the defined range
        if min < float(X) < max:
            # Add X and Y values to their respective arrays
            x.append((float(X)-min)/1000.0)
            y.append(float(Y))

# Remove the first element from x and y arrays (initial values)
x = x[1:]
y = y[1:]

# Apply the Savitzky-Golay filter to the data
window_size = 51
order = 10
y_savitzky = savgol_filter(y, window_size, order)

# Plot the original and filtered data
plt.plot(x, y, label='Original data')
plt.plot(x, y_savitzky, label='Savitzky-Golay')
plt.title("Loki's thrust curve")
plt.xlabel("Time (s)")
plt.ylabel("Thrust (N)")
plt.grid()
plt.legend()

# Calculate the area under the curve using the trapezoidal rule
area = np.trapz(y, x)

# Print the area
print("Total Impulse:", area, "Ns")

# Display the plot
plt.show()

# Code for generating blue or red dots depending on which "side" they fall of a reference line

import numpy as np
import matplotlib.pyplot as plt

N = 100

# Generates list with N entries for blue and red dots
blues_x = np.zeros(N)
blues_y = np.zeros(N)
reds_x = np.zeros(N)
reds_y = np.zeros(N)

# Blue and red counters
a = 0
b = 0

# Generates a random pair of coordinates for drawing the reference line
point1 = np.random.uniform(-1,1,2)
point2 = np.random.uniform(-1,1,2)
# Finds the line coefficients
coefs_line = np.array([(point2[1]-point1[1])/(point2[0]-point1[0]),point2[1]-(point2[0]*(point2[1]-point1[1])/(point2[0]-point1[0]))]) #f = angular*x + linear
# Generates each point (x_0, x_1, x_2)
x = np.random.uniform(-1,1,(N,3))  # initializes point coordinates and x_0s but without setting x_0 = 1
# y will be either 1 (blue) or -1 (red)
y = np.zeros(N)
# Sets x0 of each line as 1 and sets yn values (1 or -1) according to the generated function
# If yn > line it will be blue, otherwise it will be red
for i in range(0,N):
    x[i][0] = 1
    if x[i][2] > coefs_line[0]*x[i][1] + coefs_line[1]:
        y[i] = 1
        blues_x[a] = x[i][1]
        blues_y[a] = x[i][2]
        a = a + 1
    if x[i][2] < coefs_line[0]*x[i][1] + coefs_line[1]:
        y[i] = -1
        reds_x[b] = x[i][1]
        reds_y[b] = x[i][2]
        b = b + 1

# Clears remaining zeros (N - actual_points)
blues_x = np.trim_zeros(blues_x)
blues_y = np.trim_zeros(blues_y)
reds_x = np.trim_zeros(reds_x)
reds_y = np.trim_zeros(reds_y)

# Creates reference points to plots the reference line
axis_x = np.linspace(-1,1,50)
axis_y = np.zeros(len(axis_x))
for i in range(0,len(axis_x)):
    axis_y[i] = coefs_line[0]*axis_x[i] + coefs_line[1]

# Plot results
plt.plot(axis_x, axis_y, linewidth = 2, color = 'k', linestyle = '--')
plt.scatter(blues_x, blues_y, c='b')
plt.scatter(reds_x, reds_y, c='r')
plt.xlim(-1.1,1.1)
plt.ylim(-1.1,1.1)
plt.show()

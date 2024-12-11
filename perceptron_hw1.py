import sys
import numpy as np
import matplotlib.pyplot as plt

# We have a 2D space ranging from -1 to 1 in both dimensions
# Let's repeat the process M times for N points
M = 1000
N = 10
threshold = 1000

# Fixing the numpy sign function
def sign_function(arg):
    if np.sign(arg) == 1:
        return 1
    if np.sign(arg) == 0:
        return 1
    if np.sign(arg) == -1:
        return -1

def generator():
    # Generates trget function fro mtwo random points in space
    point1 = np.random.uniform(-1,1,2)
    point2 = np.random.uniform(-1,1,2)
    coefs_line = np.array([(point2[1]-point1[1])/(point2[0]-point1[0]),point2[1]-(point2[0]*(point2[1]-point1[1])/(point2[0]-point1[0]))]) #f = coefs_line[0]*x + coefs_line[1]
    # Generating xn and yn
    global x
    global y
    x = np.random.uniform(-1,1,(N,3))
    y = np.zeros(N)
    # Sets x0 as 1 and yn (feature) as 1 or -1
    for i in range(0,N):
        x[i][0] = 1
        if x[i][2] > coefs_line[0]*x[i][1] + coefs_line[1]:
            y[i] = 1
        if x[i][2] < coefs_line[0]*x[i][1] + coefs_line[1]:
            y[i] = -1

# Counts misclassified points and updates the list
def wrong():
    global misclassified
    misclassified = []
    for j in range(0,N):
        if sign_function(np.inner(w,x[j])) != y[j]:
            misclassified.append(j)
    return len(misclassified)

iterations = np.zeros(M)

for i in range(0,M):
    w = np.zeros(3)
    generator()
    k = 0
    wrong()
    # While we still have misclassified points we keep the script running
    while len(misclassified) > 0:
        index = int(np.random.uniform(0,len(misclassified)-1,1))
        w = w + y[misclassified[index]]*x[misclassified[index]]
        k = k+1
        wrong()
        # Error message if it takes longer than threshold repeats
        if k > threshold:
            print('Stopped after repeat ' + str(i) + ' took longer than ' + str(threshold) + ' iterations.')
            sys.exit()
    iterations[i] = k

bins_vector = np.linspace(0.0, 200.0, num=50)
plt.hist(iterations, bins = bins_vector, facecolor='b', alpha=0.75)
plt.text(100, 350, 'Maximum of iterations: ' + str(int(np.max(iterations))))
plt.text(100, 300, 'Mean of iterations: ' + str(int(np.mean(iterations))))
plt.xlabel('Iterations until convergence')
plt.ylabel('Occurences')
plt.xlim(0,200)
plt.show()

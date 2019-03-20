import csv
from sklearn.metrics import r2_score
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

power=[330, 345, 360]*4
speed=[1000]*3+[1100]*3+[1200]*3+[1300]*3
matrixX=[]
#density=[99.879, 99.908, 99.9, 99.901, 99.898, 99.911, 99.932, 99.936, 99.854, 99.907, 99.911, 99.918]
density=[200, 200, 200, 220, 220, 220, 240, 240, 240, 260, 260, 260]
#vectorY=np.array(density)
# set matrix of X
for item in range(12):
    matrixX.append([1]+[power[item]]+[speed[item]]+[power[item]*speed[item]]+[power[item]/speed[item]])

# calculating paramters of normal equation:
# final - coefficients in regression model
# equation final=(X^T*X)^-1*(X^T*y)
matrixX=np.array(matrixX)
vectorY=np.array(density)
matrixXT=matrixX.transpose()
inverrr=np.linalg.inv(matrixXT.dot(matrixX))
final=inverrr.dot(matrixXT.dot(vectorY))

# function from regression model coefficients
def func(powr, sped):
    return final[0]+final[1]*powr+final[2]*sped+final[3]*powr*sped+final[4]*powr/sped
# vectorisation of func for plotting
vfunc = np.vectorize(func)
# Predicted values of density from regression model
densityPredict=[]
for item in range(12):
    densityPredict.append(func(power[item],speed[item]))

# R^2 coefficient
print(r2_score(density, densityPredict))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot predicted function
X = np.arange(330, 360, 2)
Y = np.arange(1000, 1300, 20)
X, Y = np.meshgrid(X, Y)
Z=vfunc(X,Y)
# Plot real values as points
ax.scatter(power, speed, density, c='r', marker='o')
ax.plot_surface(X, Y, Z, color='b')

plt.show()

import csv
import matplotlib as mpl
from sklearn.metrics import r2_score
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# reading experimental data from csv into experiments dictionary
experiments={}
with open('for_regression.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lis=[]
        for eid in [445,446,447,448,449,450,458]:
            try:
                lis.append(float(row['PI'+str(eid)].replace(',','.')))
            except:
                pass #print('cube '+row['cube']+' has missing values' )
        if int(row['cube']) in experiments:
            experiments[int(row['cube'])]=experiments[int(row['cube'])]+lis
        else:
            experiments[int(row['cube'])]=lis
        
# splitting experiments dictionary into average POROSITY and 95% confidence interval
aver={}
erro={}
for key, value in experiments.items():
    aver[key]=np.mean(value)
    erro[key]=stats.sem(value)*1.96
    
# reading parameters from csv into param dict
param={}
with open('parameters.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row['cube']) in experiments:
            param[int(row['cube'])]=[float(row['power']),float(row['hatch'].replace(',','.')),float(row['speed'])]

# creating vector Y and matrix X for normal equation
vectorY=[]
matrixX=[]
for key, value in aver.items():
    vectorY.append(100-aver[key])
    # Matrix can be adjusted for the best model *******
    matrixX.append([1]+param[key]+[param[key][0]*param[key][1]]+[param[key][0]*param[key][2]]\
                   +[param[key][1]*param[key][2]]\
                   +[param[key][0]*param[key][1]*param[key][2]])

# Elements of normal equation    
matrixX=np.array(matrixX)
vectorY=np.array(vectorY)
matrixXT=matrixX.transpose()
inverrr=np.linalg.inv(matrixXT.dot(matrixX))
# Solution of normal equation
final=inverrr.dot(matrixXT.dot(vectorY))

#print(final)
# Function that predicts density basing on list of parameters
# here par - list of the form [Laser Power, Hatch, Scan speed]
def solut(par):
    # adjust function according to matrix form from ******
    return final[0]+final[1]*par[0]+final[2]*par[1]+final[3]*par[2] \
           +par[0]*par[1]*final[4]+par[0]*par[2]*final[5]+par[1]*par[2]*final[6]+final[7]*par[0]*par[1]*par[2]

# function for plotting nice thesis graphics
def solut2(powr,sped):
    return solut([powr,0.1,sped])   
vfunc = np.vectorize(solut2)

# For plotting
x=[]
y=[]
yc=[]
e=[]

def plotcont():
    x = np.linspace(300, 370, 100)
    y = np.linspace(1000, 2000, 100)
    X, Y = np.meshgrid(x, y)
    Z = solut2(X, Y)
    plt.figure()
    contourplot = plt.contourf(X,Y,Z, cmap=plt.cm.bone,
                  origin='lower')
    
##ax.set_xlabel('Laser power [W]', )
##ax.set_ylabel('Scan speed [mm/s]', )
    
    cbar = plt.colorbar(contourplot)
    plt.xlabel('Laser power [W]', )
    plt.ylabel('Scan speed [mm/s]', )



 
for key, value in param.items():
   # print('known: ' + str(round(100-aver[key],3))+' calc: '\
    #+str(round(solut(value),3)) + ' diff ' + str(round(100-aver[key] - solut(value),3)))
    x.append(key)
    y.append(100-np.mean(experiments[key]))
    e.append(stats.sem(experiments[key])*1.96)
    yc.append(solut(value))
#print(solut([370,0.06,900]))
#print(solut([10,0.2,30000]))
#plt.errorbar(x, y, e, linestyle='--', label='ID '+ str(key))
#plt.plot(x,yc,'o')
X = np.arange(300, 380, 10)
Y = np.arange(1000, 2050, 50)
X, Y = np.meshgrid(X, Y)
Z=vfunc(X,Y)


#mpl.rcParams['legend.fontsize'] = 10
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

fig = plt.figure()
ax = fig.gca(projection='3d')
print(r2_score(y, yc))
print(final)
ax.plot_wireframe(X, Y, Z, color='b',label='Predicted model $R^2=$'+str("%.2f" % round(r2_score(y, yc),2)))
power=[]
speed=[]
density=[]
for key, value in param.items():
    if value[1]==0.1:
     #   print(value)
        power.append(value[0])
        speed.append(value[2])
        density.append(100-aver[key])
        
ax.scatter(power, speed, density, c='r', marker='o', label='Experimental')
ax.set_zlabel('Relative density [%]', )
ax.set_xlabel('Laser power [W]', )
ax.set_ylabel('Scan speed [mm/s]', )
ax.legend()

print(solut([300,0.1,3000]))
print(100-aver[50])

#plotcont()

plt.show()



















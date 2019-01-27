import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
experiments={}
with open('for_regression.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lis=[]
        for eid in [445,446,447,448,449,450,458]:
            try:
                lis.append(float(row['PI'+str(eid)].replace(',','.')))
            except:
                print('cube '+row['cube']+' has missing values' )
        if int(row['cube']) in experiments:
            experiments[int(row['cube'])]=experiments[int(row['cube'])]+lis
        else:
            experiments[int(row['cube'])]=lis
        

aver={}
erro={}

for key, value in experiments.items():
    aver[key]=np.mean(value)
    erro[key]=stats.sem(value)*1.96
    


param={}
with open('parameters.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row['cube']) in experiments:
            param[int(row['cube'])]=[float(row['power']),float(row['hatch'].replace(',','.')),float(row['speed'])]
            
vectorY=[]
matrixX=[]

for key, value in aver.items():
    vectorY.append(100-aver[key])
    matrixX.append([1]+param[key]+[param[key][0]/param[key][1]/param[key][2]])

    
matrixX=np.array(matrixX)
vectorY=np.array(vectorY)
matrixXT=matrixX.transpose()
inverrr=np.linalg.inv(matrixXT.dot(matrixX))
final=inverrr.dot(matrixXT.dot(vectorY))

print(final)

def solut(par):
    return final[0]+final[1]*par[0]+final[2]*par[1]+final[3]*par[2]+final[4]*par[0]/par[1]/par[2]

x=[]
y=[]
yc=[]
e=[]
 
for key, value in param.items():
   # print('known: ' + str(round(100-aver[key],3))+' calc: '\
    #+str(round(solut(value),3)) + ' diff ' + str(round(100-aver[key] - solut(value),3)))
    x.append(key)
    y.append(100-np.mean(experiments[key]))
    e.append(stats.sem(experiments[key])*1.96)
    yc.append(solut(value))
print(solut([370,0.06,900]))
print(solut([10,0.2,30000]))
plt.errorbar(x, y, e, linestyle='--', label='ID '+ str(key))
plt.plot(x,yc,'o')

plt.show()
    















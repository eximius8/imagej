import csv
import numpy as np
import matplotlib.pyplot as plt
experiments={}
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for Eid in [445,446,447,448,449,450,451]:
            try:
                if (Eid, int(row["S"+ str(Eid)])) in experiments:                    
                    experiments[(Eid, int(row["S"+ str(Eid)]))].append(float(row["HV"+ str(Eid)]))
                elif row["S"+ str(Eid)]:                    
                    experiments[(Eid, int(row["S"+str(Eid)]))]=[float(row["HV"+ str(Eid)])]
            except:
                pass

plotpar={}
for key, value in experiments.items():
    if key[0] != 458 and key[1] in plotpar:
        plotpar[key[1]].append([(key[0]-445)*200, np.mean(value),np.std(value)])
    elif key[0] != 458:
        plotpar[key[1]]=[[(key[0]-445)*200, np.mean(value),np.std(value)]]

        
for key, value in plotpar.items():
    plotpar[key].sort()



for key, value in plotpar.items():
    x=[]
    y=[]
    e=[]
    for cube in plotpar[key]:
        x.append(cube[0])
        y.append(cube[1])
        e.append(cube[2])
    plt.errorbar(x, y, e, linestyle='--', label='Cube '+ str(key))
plt.legend(loc='right center')

    


plt.show()

        

#print(experiments)

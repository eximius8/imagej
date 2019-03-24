import csv
from sklearn.metrics import r2_score
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

class cubes:
    def __init__(self,par_list,cube_list):
        self.cubes=cube_list
        self.param=par_list
        
    def vectY(self,start, end):
        y=[]
        for i in range(start,end):
            y.append(self.cubes[i])
        return y
    def matrX(self, start, end):
        x=[]
        for i in range(start,end):
            x.append(self.param[i])
        return x

class regresss:
'''This class is for regression analysis it takes matrix of parameters and vector of outputs and solves normal equation
the fitted model or hypothesis function is labeled with ****'''
    def __init__(self,parametri,density):
        def model(self,param):
            ''' takes a list of parameters, adjusts the list according to hypothesis function
                returns a list according to hypothesis function'''
            powr=param[0]
            hatch=param[1]
            sped=param[2]
            model=[1, powr, sped**2, powr/sped,powr*sped] #**** fitted model (hypothesis function) in the form of list
            return model
        self.model=model # make model an instance of this class
        self.parametri=parametri        
        self.vectrY=np.array(density) 
        self.matrixAX=[]
        for i in range(len(self.parametri)):
            self.matrixAX.append(self.model(self,self.parametri[i]))
        # solution of normal equation (self.theta is a list with model coefficients):
        self.matrixAX=np.array(self.matrixAX)
        self.matrixAXT=self.matrixAX.transpose()
        inverrr=np.linalg.inv(self.matrixAXT.dot(self.matrixAX))
        self.theta=inverrr.dot(self.matrixAXT.dot(self.vectrY))
        
    def theta(self):
        # returns solution to normal equation in the form of a list
        return self.theta
    
    def predictX(self):
        # returns vector of values predicted by the hypothesis function for initial list of parameters self.parametri
        prediction=[]
        for i in range(len(self.parametri)):
            prediction.append(self.predict(self.parametri[i]))
        return prediction

    def predict(self,param):
        # returns calculated with hypothesis function value of output for given list of parameters (param)
        return sum([x * y for x, y in zip(self.model(self,param),self.theta)])
    
    def r2(self):
        # returns coefficient of correlation for hypothesis function
        return r2_score(self.vectrY,self.predictX())
        
        
def archimedes_read():
# read csv file with raw Archimedes measurements
# returns array with cube number as index and a list with 3 relative densitites (relative_density)
# return average of three relative densities for three measurements (rel_dens_av)
    real_density={}
    max_realD1,max_realD2,max_realD3=0,0,0    
    relative_density={}
    rel_dens_av={}
    with open('archim536_raw.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        row1 = next(reader)
        rhoAir=float(row1['mAir'])
        rhoAc1=float(row1['mAc1'])
        rhoAc2=float(row1['mAc2'])
        rhoAc3=float(row1['mAc3'])       
        for row in reader:
            mAir=float(row['mAir'])
            mAc1=float(row['mAc1'])
            mAc2=float(row['mAc2'])
            mAc3=float(row['mAc3'])
            realD1=(rhoAc1-rhoAir)*mAir/(mAir-mAc1)+rhoAir            
            realD2=(rhoAc2-rhoAir)*mAir/(mAir-mAc2)+rhoAir
            realD3=(rhoAc3-rhoAir)*mAir/(mAir-mAc3)+rhoAir
            if realD1>max_realD1:
                max_realD1=realD1
            if realD2>max_realD2:
                max_realD2=realD2
            if realD3>max_realD3:
                max_realD3=realD3
            real_density[int(row['Sample'])]=[realD1,realD2,realD3]
    for key,value in real_density.items():
        relative_density[key]=[value[0]/max_realD1, value[1]/max_realD2, value[2]/max_realD3]
        rel_dens_av[key]=(value[0]/max_realD1+value[1]/max_realD2+value[2]/max_realD3)/3.
    return rel_dens_av#relative_density

def parameter_read():
# returns paraemters dictionary with cube number as index and list of the form [Power, Hatch, Speed]
    parameters={}
    with open('parameters.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            parameters[int(row['Cube'])]=[float(row['Power']), \
                                          float(row['Hatch']), \
                                          float(row['Speed'])]
    return parameters



sett=cubes(parameter_read(),archimedes_read())
regr112=regresss(sett.matrX(25,37),sett.vectY(25,37))
#regr112.predict([200,0.1,1400])
print(regr112.r2())

#print(regress_calc(cubes.matrX,cubes.vectY))


##y_predicted=[]
##y_real=[]
##theta=regress_calc(parameter_read(),archimedes_read())
##for key, value in parameter_read().items():
##    y_predicted.append(regress_predict(value,theta))
##    y_real.append(archimedes_read()[key])
##
##print(r2_score(y_real, y_predicted))
###print(y_predicted)            

    

#print(regress_calc(parameter_read(),archimedes_read()))

    

##power=[330, 345, 360]*4
##speed=[1000]*3+[1100]*3+[1200]*3+[1300]*3
##matrixX=[]
##density=[99.879, 99.908, 99.9, 99.901, 99.898, 99.911, 99.932, 99.936, 99.854, 99.907, 99.911, 99.918]
###density=[200, 200, 200, 220, 220, 220, 240, 240, 240, 260, 260, 260]
###vectorY=np.array(density)
### set matrix of X
##for item in range(12):
##    matrixX.append([1]+[power[item]]+[speed[item]]+[power[item]*speed[item]]+[power[item]/speed[item]])
##
### calculating paramters of normal equation:
### final - coefficients in regression model
### equation final=(X^T*X)^-1*(X^T*y)
##matrixX=np.array(matrixX)
##vectorY=np.array(density)
##matrixXT=matrixX.transpose()
##inverrr=np.linalg.inv(matrixXT.dot(matrixX))
##final=inverrr.dot(matrixXT.dot(vectorY))
##
### function from regression model coefficients
##def func(powr, sped):
##    return final[0]+final[1]*powr+final[2]*sped+final[3]*powr*sped+final[4]*powr/sped
### vectorisation of func for plotting
##vfunc = np.vectorize(func)
### Predicted values of density from regression model
##densityPredict=[]
##for item in range(12):
##    densityPredict.append(func(power[item],speed[item]))
##
### R^2 coefficient
##print(r2_score(density, densityPredict))
##
##fig = plt.figure()
##ax = fig.add_subplot(111, projection='3d')
##
### Plot predicted function
##X = np.arange(330, 360, 2)
##Y = np.arange(1000, 1300, 20)
##X, Y = np.meshgrid(X, Y)
##Z=vfunc(X,Y)
### Plot real values as points
##ax.scatter(power, speed, density, c='r', marker='o')
##ax.plot_surface(X, Y, Z, color='b')
##
##plt.show()

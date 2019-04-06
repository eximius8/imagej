from sklearn.metrics import r2_score
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from reading_data import *

class cubes:
    def __init__(self,par_list,cube_list):
        self.cubes=cube_list
        self.param=par_list
        self.STDflag=False
        if type(cube_list[1]) is list:
            self.STDflag=True
        
    def vectY(self,start, end):
        y=[]
        for i in range(start,end):
            if self.STDflag:
                y.append(self.cubes[i][0])
            else:
                y.append(self.cubes[i])
        return y
    
    def vectSTD(self,start, end):
        if not self.STDflag:
            raise NameError('No STD was found')
        seem=[]
        for i in range(start,end):
            seem.append(self.cubes[i][1])
        return seem
    
    def matrX(self, start, end):
        x=[]
        for i in range(start,end):
            x.append(self.param[i])
        return x
    def plt_2dd(self, num_list, Flag):
        # plots 2D plot of Relative density vs Power (Flag=0) or hatch (Flag=1) or speed (Flag=2) 
        # num_list - list of cube IDs
        y=[]
        x=[]
        for item in num_list:
            y.append(self.cubes[item])
            x.append(self.param[item][Flag])
        fig = plt.figure()
        plt.plot(x,y)
        plt.show()
        
            

class regresss:
#This class is for regression analysis it takes matrix of parameters and vector of outputs and solves normal equation
#the fitted model or hypothesis function is labeled with ****'''
    def __init__(self,parametri,density):
        def model(self,param):
#  takes a list of parameters, adjusts the list according to hypothesis function
#  returns a list according to hypothesis function'''
            powr=param[0]
            hatch=param[1]
            sped=param[2]
            self.modell=[1,powr,sped]# sped**2, powr/sped,powr*sped] #**** fitted model (hypothesis function) in the form of list
            return self.modell
        self.model=model # make model an instance of this class
        self.parametri=parametri
        self.density=density
       # print(self.density)
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
    def r2_adj(self):
        #returns adjusted R^2 n - sample size p - number of parameters
        n=len(self.parametri)
        p=len(self.modell)-1
        return 1-(1-self.r2())*(n-1)/(n-p-1)
    
    def plt_3dd(self):
        # plots 3d plot of hypothesis function with experimental points as dots
        Pmax=0
        Pmin=1000
        vmax=0
        vmin=1000000000000
      #  print(self.parametri)
        power=[]
        speed=[]
        for value in self.parametri:
            power.append(value[0])
            speed.append(value[2])
            if value[0]>Pmax:
                Pmax=value[0]
            if value[0]<Pmin:
                Pmin=value[0]
            if value[2]>vmax:
                vmax=value[2]
            if value[2]<vmin:
                vmin=value[2] 
       #print(vmin)
        X = np.arange(Pmin, Pmax+2, 2)
        Y = np.arange(vmin, vmax+10, 10)
        X, Y = np.meshgrid(X, Y)
        def func(p,v):
            return self.predict([p,0.2,v])
        vfunc = np.vectorize(func)
        Z=vfunc(X,Y)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
### Plot real values as points
        ax.scatter(power, speed, self.vectrY, c='r', marker='o')
        ax.plot_surface(X, Y, Z, color='b')
        plt.show()

    def plt_count(self):
        # plots countor plot of hypothesis function with experimental points as dots
        Pmax=0
        Pmin=1000
        vmax=0
        vmin=1000000000000
      #  print(self.parametri)
        power=[]
        speed=[]
        for value in self.parametri:
            power.append(value[0])
            speed.append(value[2])
            if value[0]>Pmax:
                Pmax=value[0]
            if value[0]<Pmin:
                Pmin=value[0]
            if value[2]>vmax:
                vmax=value[2]
            if value[2]<vmin:
                vmin=value[2] 
        #print(vmin)
        X = np.arange(Pmin, Pmax+2, 2)
        Y = np.arange(vmin, vmax+10, 10)
        X, Y = np.meshgrid(X, Y)
        def func(p,v):
            return self.predict([p,0.2,v])
        vfunc = np.vectorize(func)
        Z=func(X,Y)
        fig = plt.figure()
        contourplot = plt.contourf(X,Y,Z, cmap=plt.cm.bone,
                  origin='lower')
### Plot real values as points
        cbar = plt.colorbar(contourplot)
        plt.xlabel('Laser power [W]', )
        plt.ylabel('Scan speed [mm/s]', )
        plt.show()

   
        
        

#sett=cubes(parameter_read(),archimedes_read())

flagg=True
suffix='P_ab_100px'#'BP'#'BP'
set1=cubes(parameter_read(),micro_read('ID536'+suffix+'.csv',flagg))
set2=cubes(parameter_read(),micro_read('ID537'+suffix+'.csv',flagg))
set3=cubes(parameter_read(),micro_read('ID538'+suffix+'.csv',flagg))
set4=cubes(parameter_read(),micro_read('ID539'+suffix+'.csv',flagg))
#set5=cubes(parameter_read(),micro_read('ID539BP.csv'))
set6=cubes(parameter_read(),micro_read('ID540'+suffix+'.csv',flagg))
#set7=cubes(parameter_read(),micro_read('ID540BP.csv'))
set8=cubes(parameter_read(),micro_read('ID541'+suffix+'.csv',flagg))
#set9=cubes(parameter_read(),micro_read('ID541BP.csv'))



#print(micro_read('ID540P.csv'))
#print(parameter_read())
#fig = plt.figure()
        
        
i=536
sets={
    '1000 ppm': set1,
    '800 ppm': set2,
    '600 ppm': set3,
    '400 ppm': set4,
    '200 ppm': set6,
    '0 ppm': set8
}
##markerr=6
for key,sett in sets.items():
##    y=sett.vectY(37,43)
##    x=[]
##    for paramet in sett.matrX(37,43):
##        x.append(paramet[2])
##    plt.errorbar(x, y, sett.vectSTD(37,43),label=key,marker=markerr)
##    markerr=markerr+1

##for key,sett in sets.items():
##    y=sett.vectY(43,49)
##    x=[]
##    for paramet in sett.matrX(43,49):
##        x.append(paramet[1])
##    #plt.plot(x,y,label=key,marker=markerr)
##    
##    plt.errorbar(x, y, sett.vectSTD(43,49),label=key,marker=markerr)
##    markerr=markerr+1
##   # print(sett.vectSTD(43,49))
##    #print(sett.vectY(43,49))
#plt.legend()

#plt.show()

    regr112=regresss(sett.matrX(1,13),sett.vectY(1,13))
    regr=regresss(sett.matrX(1,37),sett.vectY(1,37))
    regr1324=regresss(sett.matrX(13,25),sett.vectY(13,25))
    regr2536=regresss(sett.matrX(25,37),sett.vectY(25,37))
    print(i)
    #print(sett.matrX(37,44))
    
    i=i+1
    #print(regr.r2())
    #print(regr.r2_adj())
    print(regr112.r2())
    print(regr112.r2_adj())
    print(regr1324.r2())
    print(regr1324.r2_adj())
    print(regr2536.r2())
    print(regr2536.r2_adj())
   # regr2536.plt_count()

#plt.show()

#set1.plt_2dd([37,38,39,40,41,42],2)
#set2.plt_2dd([37,38,39,40,41,42],2)
#set3.plt_2dd([37,38,39,40,41,42],2)
#set4.plt_2dd([37,38,39,40,41,42],2)
#set5.plt_2dd([37,38,39,40,41,42],2)
#set6.plt_2dd([37,38,39,40,41,42],2)
#set7.plt_2dd([37,38,39,40,41,42],2)
#set8.plt_2dd([37,38,39,40,41,42],2)
#set9.plt_2dd([37,38,39,40,41,42],2)

#set1.plt_2dd([43,44,45,46,47,48],1)
#set2.plt_2dd([43,44,45,46,47,48],1)
#set3.plt_2dd([43,44,45,46,47,48],1)
#set4.plt_2dd([43,44,45,46,47,48],1)
#set5.plt_2dd([43,44,45,46,47,48],1)
#set6.plt_2dd([43,44,45,46,47,48],1)
#set7.plt_2dd([43,44,45,46,47,48],1)
#set8.plt_2dd([43,44,45,46,47,48],1)
#set9.plt_2dd([43,44,45,46,47,48],1)


#regr112.plt_3dd()


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


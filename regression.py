from sklearn.metrics import r2_score
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from reading_data import *
import itertools
from pandas import DataFrame
from sklearn import linear_model
import statsmodels.api as sm

class regresss:
#This class is for regression analysis it takes matrix of parameters and vector of outputs and solves normal equation
#the fitted model or hypothesis function is labeled with ****'''
    def __init__(self,parametri,density,model_list):
        self.model_list=model_list
        def model(self,param):
#  takes a list of parameters, adjusts the list according to hypothesis function
#  returns a list according to hypothesis function'''
            powr=param[0]
            hatch=param[1]
            sped=param[2]
            self.modell=eval(self.model_list)#[1,powr,hatch,sped,powr/hatch/sped]# sped**2, powr/sped,powr*sped] #**** fitted model (hypothesis function) in the form of list
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
        self.olsmodel = sm.OLS(self.vectrY, self.matrixAX).fit()
        self.theta=self.olsmodel.params
        
        #predictions = model.predict(X)
##        self.matrixAXT=self.matrixAX.transpose()
##        inverrr=np.linalg.inv(self.matrixAXT.dot(self.matrixAX))
##        self.theta=inverrr.dot(self.matrixAXT.dot(self.vectrY))
        
    def thetaa(self):
        # returns solution to normal equation in the form of a list
        return self.theta
    def moddd(self):
        return self.olsmodel
    
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
            return self.predict([p,0.1,v])
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

   
##print(parameter_read('Scalmalloy/parameters.csv'))
##cubes_in_sc=micro_read('Scalmalloy/for_regression.csv',IDD='PI458').keys()
#print(micro_read('Scalmalloy/for_regression.csv',IDD='PI458'))
#print(micro_read('AlSi7Mg/ID536.csv'))
set1=cubes(parameter_read('AlSi7Mg/parameters.csv'),micro_read('AlSi7Mg/ID536.csv',False))
params_str=['sped','powr','hatch','sped**2','powr**2','hatch**2','powr/sped/hatch','powr**-1','hatch**-1','sped**-1','hatch**-2','sped**-2','powr**-2']
##modelss=itertools.combinations(params_str,4)
##models=[]
##for model in modelss:
##    lis=['1']+list(model)
##    models.append('['+",".join(lis)+']')
##    #print('['+",".join(lis)+']')
##
##for model in models:
##    for i in [445,446,447,448,449,450,458]:
##        setSc=cubes(parameter_read('Scalmalloy/parameters.csv'),micro_read('Scalmalloy/for_regression.csv',False,IDD='PI'+str(i)))
##        scregr=regresss(setSc.matrX(setSc.av_cubes()),setSc.vectY(setSc.av_cubes()),model)
##        alregr=regresss(set1.matrX(set1.av_cubes()),set1.vectY(set1.av_cubes()),model)
##        if scregr.r2()>0.9 and scregr.moddd().rsquared_adj>0.9:
##            print(str(i)+' '+model)
##            print(scregr.r2())
##            print(scregr.r2_adj())
##            print(scregr.moddd().summary())
##    #print(alregr.r2())


setSc=cubes(parameter_read('Scalmalloy/parameters.csv'),micro_read('Scalmalloy/for_regression.csv',False,IDD='PI447'))
regr = linear_model.LinearRegression()
X=setSc.matrX(setSc.av_cubes())
y=setSc.vectY(setSc.av_cubes())
regr.fit(X, y)
#print(y)
#print('Intercept: \n', regr.intercept_)
#print('Coefficients: \n', regr.coef_)
print(X)
X = sm.add_constant(X)
print(X)
model = sm.OLS(y, X).fit()
predictions = model.predict(X) 
#print(predictions) 
#print_model = model.summary()
print( model.summary())
print(model.rsquared)
print(model.rsquared_adj)
alregr=regresss(setSc.matrX(setSc.av_cubes()),y,'[1,powr,hatch,sped**-2]')
print(alregr.thetaa())
print(alregr.r2_adj())
alregr.plt_count()

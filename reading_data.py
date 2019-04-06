import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

class cubes:
    def __init__(self,par_list,cube_list):
        self.cubes=cube_list
        self.param=par_list
        self.STDflag=False
        if type(next(iter(cube_list))) is list:
            self.STDflag=True

    def av_cubes(self):
        # returns keys of available cubes
        return self.cubes.keys()
        
    def vectY(self,list_of_cubes):
        y=[]
        for i in list_of_cubes:
            if self.STDflag:
                y.append(self.cubes[i][0])
            else:
                y.append(self.cubes[i])
        return y
    
    def vectSTD(self,list_of_cubes):
        if not self.STDflag:
            raise NameError('No STD was found')
        seem=[]
        for i in list_of_cubes:
            seem.append(self.cubes[i][1])
        return seem
    
    def matrX(self, list_of_cubes):
        x=[]
        for i in list_of_cubes:
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


def parameter_read(file):
# returns parameters dictionary with cube number as index and list of the form [Power, Hatch, Speed]
    parameters={}
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                cube=int(row['Cube'])
            except:
                cube=int(row['cube'])
            try:
                power=float(row['Power'].replace(',','.'))
            except:
                power=float(row['power'].replace(',','.'))
            try:
                hatch=float(row['Hatch'].replace(',','.'))
            except:
                hatch=float(row['hatch'].replace(',','.'))
            try:
                speed=float(row['Speed'].replace(',','.'))
            except:
                speed=float(row['speed'].replace(',','.'))
            parameters[cube]=[power, hatch, speed]
    return parameters

def micro_read(file,flag=True,IDD=False):
# returns dictionary of densities
# Flag - determines what values to report, True - average measured density
# False - area or particle count
   # print(file)
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rd={}
        for row in reader:
            for value in ['Label', 'Slice','cube']:
                try:
                    cube=int(row[value][0:2])
                except:
                    pass
            for value in ['Area','Count']:
                try:
                    area=float(row[value].replace(',','.'))
                except:
                    pass
            for value in ['PArea','%Area',IDD]:
                try:
                    dens=100-float(row[value].replace(',','.'))
                except:
                    pass
            try:
                try:
                    rd[cube].append([area,dens])
                except:
                    rd[cube]=[[area,dens]]
            except:
                try:
                    rd[cube].append(dens)
                except:
                    rd[cube]=[dens]
                    
        rd_aver_m={}
        rd_aver_calc={}
        rd_std={}
        rd_area={}
        for key,value in rd.items():
            try:
                rd_aver_m[key]=value[0][1]
                rd_list=[value[1][1],value[2][1],value[3][1]]
                rd_std[key]=[np.mean(rd_list),stats.sem(rd_list)*1.96]
                rd_aver_calc[key]=np.mean(rd_list)
                rd_area[key]=value[0][0]
            except:
                rd_std[key]=[np.mean(value),stats.sem(value)*1.96]
                rd_area[key]=np.mean(value)
            #print(str(key)+" "+str(rd_aver_m[key])+" "+str(rd_aver_calc[key])+" "+str(rd_std[key][1]))
    #for key,value in rd_aver_m.items():
        #print(value)
    if flag:
        return rd_std#rd_aver_m#
    else:
        return rd_area
         
        
        
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

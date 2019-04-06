import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def parameter_read():
# returns parameters dictionary with cube number as index and list of the form [Power, Hatch, Speed]
    parameters={}
    with open('parameters.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            parameters[int(row['Cube'])]=[float(row['Power']), \
                                          float(row['Hatch']), \
                                          float(row['Speed'])]
    return parameters

def micro_read(file,flag=True):
# returns dictionary of densities
# Flag - determines what values to report, True - average measured density
# False - area or particle count
   # print(file)
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rd={}
        for row in reader:
            try:
                cube=int(row['Label'][0:2])                
            except:
                cube=int(row['Slice'][0:2])
            try:
                area=float(row['Area'])
            except:                
                area=float(row['Count'])
            try:
                dens=100-float(row['PArea'])
            except:
                dens=100-float(row['%Area'])
            try:
                rd[cube].append([area,dens])
            except:
                rd[cube]=[[area,dens]]
        rd_aver_m={}
        rd_aver_calc={}
        rd_std={}
        rd_area={}
        for key,value in rd.items():
            rd_aver_m[key]=value[0][1]
            rd_list=[value[1][1],value[2][1],value[3][1]]
            rd_std[key]=[np.mean(rd_list),stats.sem(rd_list)*1.96]
            rd_aver_calc[key]=np.mean(rd_list)
            rd_area[key]=value[0][0]
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

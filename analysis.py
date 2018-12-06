import csv
experiments={}
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for Eid in [445,446,447,448,449,450,458]:
            try:
                if (Eid, int(row["S"+ str(Eid)])) in experiments:                    
                    experiments[(Eid, int(row["S"+ str(Eid)]))].append(float(row["HV"+ str(Eid)]))
                elif row["S"+ str(Eid)]:                    
                    experiments[(Eid, int(row["S"+str(Eid)]))]=[float(row["HV"+ str(Eid)])]
            except:
                pass
                    

        

print(experiments)

import pandas as pd
import csv

#reading input file
res=pd.read_csv('d1.csv')

#userid=[x for x in res['userid']]
date=[x for x in res['date']]
duration=[x for x in res['duration']]

#replacing duration of each user with its average duration
sumn=0
cnt=0
date_new=[]
duration_new=[]
for i in range(len(duration)-1):
    if date[i]==date[i+1]:   #if it redials again 
        sumn=sumn+duration[i]
        cnt=cnt+1
    else:        #if the call ends 
        sumn=sumn+duration[i]
        cnt=cnt+1
        date_new.append(date[i])
        duration_new.append(sumn/cnt)
        sumn=0
        cnt=0

#printing lists
#print("date-")
#print(date)
#print("duartion-")
#print(duration)
#print("date-")
#print(date_new)
#print("duartion-")
#print(duration_new)

#put in csv file
with open('u1.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["date","duration"])

    
    data = list(zip(date_new,duration_new))
    for row in data:
        row = list(row)
        spamwriter.writerow(row)
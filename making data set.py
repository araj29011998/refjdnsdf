import pandas as pd
import numpy as np
import csv
import random
import math
from datetime import date, timedelta


#change this variable to cahnge userid 
u=1

#change sdate- starting date and edate- end date for this user
sdate = date(2008, 5, 1)   # start date
edate = date(2008, 5, 31)   # end date

delta = edate - sdate     

userid=[]
start_time=[]
end_time=[]
date=[]
time=[]

#for 1 user only
#assuming 45 mins as threshold value
for i in range(35):
     n=random.randint(40,45)
     prev_start=0
     prev_end=0
     flag1=0
     
     for j in range(n+1):
         flag=random.randint(1, 10)
         #start time
         if flag1==1:
             prev_start=prev_end+1
             flag1=0
         else:
             prev_start=random.uniform(prev_end,719)
             prev_start=math.ceil(prev_start)
        
          #end time
         
         if flag == 4 or flag==5:
             prev_end=prev_start+45
             flag1=1
             
         else:
             prev_end=prev_start+random.uniform(0,45)
             prev_end=math.ceil(prev_end)
         
         if prev_end>673:
             break
        
         if prev_start>=674 or prev_end>=674:
                 break
         userid.append(i+1)
         start_time.append(prev_start)
         end_time.append(prev_end)
         #date time column
         day = sdate + timedelta(days=i)
         day=day.strftime("%d/%m/%Y")
         timei=str(math.floor(float(prev_start)/float(60)))
         timei=timei+":"+str(math.floor(prev_start%60))
       #  date_time=day+" "+time
        # print(date_time)
         date.append(day)
         time.append(timei)
        
     n=random.randint(40,45)
     prev_start=720
     prev_end=720 
     flag1=0

     for j in range(n+1):
         flag=random.randint(1, 10)
         #start time
         if flag1==1:
             prev_start=prev_end+1
             flag1=0
         else:
         #start time
             prev_start=random.uniform(prev_end,1439)
             prev_start=math.ceil(prev_start)
         #end time
         if flag == 4 or flag==5:
             prev_end=prev_start+45
             flag1=1
             
         else:
             prev_end=prev_start+random.uniform(0,45)
             prev_end=math.ceil(prev_end)

         if prev_end>1394:
             break
        
         if prev_start>=1395 or prev_end>=1395:
                 break
         userid.append(i+1)
         start_time.append(prev_start)
         end_time.append(prev_end)
         
         #date time column
         day = sdate + timedelta(days=i)
         day=day.strftime("%d/%m/%Y")
         timei=str(math.floor(float(prev_start)/float(60)))
         timei=timei+":"+str(math.floor(prev_start%60))
       #  date_time=day+" "+time
        # print(date_time)
         date.append(day)
         time.append(timei)

#for printing lists         
#print("user id-")
#print(userid)
#print("start time-")
#print(start_time)
#print("end time-")
#print(end_time)


#duration calculation
duration=[]
for i in range(len(userid)):
    duration.append(end_time[i]-start_time[i])

print(duration)

#for merging calls of same user but call duration more than 45 mins
duration_new=[]
user_new=[]
i=0
while i < len(userid):
    if duration[i]==45:
        sumi=duration[i]
        while i < (len(userid)-1):
            if userid[i]==userid[i+1] and duration[i]==45:
              sumi=sumi+duration[i+1]
            if duration[i]!=45:
                break
            i=i+1
        user_new.append(userid[i])
        i=i+1
        duration_new.append(sumi)
    else:
        duration_new.append(duration[i])
        user_new.append(userid[i])
        i=i+1
 
#printing duration list       
#print(duration_new)


#adding userid
user_id=[]
for x in range(len(userid)):
    user_id.append(u)


#saving user_id , date, , time and duration with duration in csv file
pd.DataFrame({'name','age','id'}).to_csv('Data1.csv')

with open('d1.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["userid", "date", "time","duration"])

    
    data = list(zip(user_id,date,time,duration_new))
    for row in data:
        row = list(row)
        spamwriter.writerow(row)

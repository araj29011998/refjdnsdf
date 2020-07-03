import pandas as pd
import random

#input dataset of all users in single csv file 
res=pd.read_csv('combined_data_avg.csv')

#considering duration list 
A=[x for x in res['duration']]

df = pd.DataFrame({ 'duration': A})
df

#set percentile variable accordingly
percentile=0.96
#this pritns the required threshold time
print(df.duration.quantile(percentile))
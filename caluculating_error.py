import pandas as pd
from math import sqrt
from sklearn.metrics import mean_squared_error

#predicted and expected values obtained by implementing ARIMA model code on data set of each user
res=pd.read_csv('predicted_expected_values_for_all_users.csv')

#userid=[x for x in res['userid']]
predicted=[x for x in res['predicted']]
expected=[x for x in res['expected']]

#caluculating RMSE value 
error = sqrt(mean_squared_error(predicted, expected))

print(error)
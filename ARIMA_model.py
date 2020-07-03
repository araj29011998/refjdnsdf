from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from pandas.plotting import autocorrelation_plot
from pandas import DataFrame
from math import sqrt

#for making date time format 
def parser(x):
	return datetime.strptime(x, '%d/%m/%Y')

#reading csv file input
series = read_csv('u1.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)

#prints 5-6 upper values
#print(series.head())

#simple series-plot input data 
series.plot()

#auto correlation for differencing 
autocorrelation_plot(series)

pyplot.show()

# fit model
model = ARIMA(series, order=(3,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())
# plot residual errors
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
residuals.plot(kind='kde')
pyplot.show()
print(residuals.describe())


#forecasting dataset by taking required train and test dataseet
X = series.values
size = int(len(X) * 0.90)  #making test set as 10% of total size
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
	model = ARIMA(history, order=(3,1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))
error = sqrt(mean_squared_error(test, predictions))  #RMSE value
print('Test RMSE: %.3f' % error)

# plotting predicted and expected values 
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.svm import SVC
from sklearn import preprocessing

def input():
	#-----------input-------
	datafile="RS1nnz_10000label.csv"
	data = pandas.read_csv(datafile)
	data=data[data.label == 'good']
	return data

def preprocess(data):	

	#-----------------Convert nominal to numeric:---------
	#data['matrix_name'] = data.matrix_name.astype('category')
	data['label'] = data.label.astype('category')
	cat_columns = data.select_dtypes(['category']).columns
	data[cat_columns] = data[cat_columns].apply(lambda x: x.cat.codes)

	#-----------------Push time to last and remove outliers ----------------------------

	cols = list(data.columns.values) #Make a list of all of the columns in the df
	cols.pop(cols.index('time')) #Remove time from list
	data = data[cols+['time']] #Create new dataframe with columns in the order you want
	data=data.dropna()
	data=data[data.time < 1e308]

	#----------------Convert data types to float-----------
	for i in cols:
		data[i]=data[i].astype(np.float64)
	#----------------Train test split:------------
	a = len(data.T) - 1 # The last column is the label
	X = data.iloc[:, list(range(0,a))]
	Y = data.iloc[:,a]
	x=pandas.DataFrame(X)
	y=pandas.DataFrame(Y)


	indices=np.arange(len(data))
	data['time']=data['time']
	data.insert(loc=0, column='index', value=indices)
	data.to_csv('data.csv',na_rep='NaN',index=False)

	X_train, X_test, Y_train, Y_test, indices_train, indices_test = train_test_split(x,y,indices, test_size = 0.34)


	# Y_test = pandas.read_csv('y_test.csv')
	# Y_train = pandas.read_csv('y_train.csv')
	# X_test = pandas.read_csv('x_test.csv')
	# X_train = pandas.read_csv('x_train.csv')
	# indices_train=pandas.read_csv('indices_train.csv')
	# indices_test=pandas.read_csv('indices_test.csv')

	Y_test['label']=X_test['label']
	Y_test_temp=Y_test
	Y_train_temp=Y_train
	X_test_temp=X_test
	X_train_temp=X_train


	#----------------fit ridge model:-----------
	print("fitting model...")
	min_max_scaler = preprocessing.MinMaxScaler()
	X_scaled = min_max_scaler.fit_transform(X_train)
	Y_scaled = min_max_scaler.fit_transform(Y_train)

	np.savetxt('ytest.csv', X_scaled, delimiter=',')
	#reg = LinearRegression().fit(X_scaled, Y_scaled)
	model=Ridge(alpha = 1,fit_intercept=True).fit(X_train, Y_train['time'])
	pred=model.predict(X_test)

preprocess(input())

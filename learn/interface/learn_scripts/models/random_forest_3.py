# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:25:40 2017
@author: A
"""

#This code is the random forest code for the different files given 
#Hopefully this works 
#Reference: https://jasdumas.github.io/2016-05-04-RF-in-python/
#Begin Code: 
import pandas 
import numpy as np

import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import datasets
#from sklearn.tree import export_graphviz
from sklearn.metrics import confusion_matrix
import six
from sklearn import tree
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import time
import sqlite3
import sys
import json

# #----------------------------------
# if len(sys.argv) != 2:
#     print("usage: python {} datafile.csv".format(sys.argv[0]))
#     sys.exit(2)
# datafile = sys.argv[1]
# #----------------------------------------

#datafile="interface/learn_scripts/datasets/classifier_bfs.csv"

def main(datafile): 
    target_names = ['good','bad']


    #print(a)
    #Begin actual Code: 

    data = pandas.read_csv(datafile)
    data = data[data.runtime != 0]


    #--------------------classify dataset as good or bad
    classification=[]
    # m=data['runtime'].mean()
    # print m
    # for index, row in data.iterrows():
    #     if row['runtime'] < m:
    #         row['classification']='good'
    #         classification.append(row['classification'])
    #     else:
    #         row['classification']='bad'
    #         classification.append(row['classification'])

    #-------------------------------
    m = data['nedges'].divide(data['runtime']).mean()
    #print(m)
    #print data['runtime']
    for index, row in data.iterrows():
        if row['nedges']/row['runtime'] < m/1000:
            row['classification']='good'
            classification.append(row['classification'])
        else:
            row['classification']='bad'
            classification.append(row['classification'])
    #----------------------------------------------------------------------Create db table
    data['classif']=pandas.Series(classification)
    cxn = sqlite3.connect('db.sqlite3')
    data.to_sql('learning_set1', con=cxn, if_exists='replace')

    #print classification

    data['package'] = data.package.astype('category')
    data['algorithm'] = data.algorithm.astype('category')
    data['dataset'] = data.dataset.astype('category')
    cat_columns = data.select_dtypes(['category']).columns
    data[cat_columns] = data[cat_columns].apply(lambda x: x.cat.codes)
    data=data.dropna()
    #data=data.drop(['runtime'], axis=1)
    #----------------------------------------------- Fit classifier


    a = len(data.T) - 1
    X = data.iloc[:,0:a] #the predictor class
    #print(X)
    Y = data.iloc[:,a] # The solutions 
    #print(Y)
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.34)
    #print((X_train.shape, X_test.shape, Y_train.shape, Y_test.shape))
    classifier = RandomForestClassifier(n_estimators = 100)
    classifier = classifier.fit(X_train, Y_train)
    #print(classifier)
    predictions = classifier.predict(X_test)

    #result = recall_score(Y_test, predictions, average = 'weighted')
    results = metrics.classification_report(Y_test, predictions, target_names)

    #---------------------------------- Analysis



    importances = classifier.feature_importances_
    std = np.std([tree.feature_importances_ for tree in classifier.estimators_],
                 axis=0)
    indices = np.argsort(importances)[::-1]
    x_lab = ['INFO', 'CUISINE', 'TYPE_OF_PLACE', 'DRINK', 'PLACE', 'MEAL_TIME', 'DISH', 'NEIGHBOURHOOD']

    # Print the feature ranking
    #print("Confusion Matrix:")

    #for f in range(X.shape[1]):
        #print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

    # Plot the feature importances of the forest

    plt.figure()
    plt.title("Feature importances")
    plt.xlabel('x_lab')
    plt.bar(list(range(X.shape[1])), importances[indices],
           color="r", yerr=std[indices], align="center")
    plt.xticks(list(range(X.shape[1])), indices)
    plt.xlim([-1, X.shape[1]])
    #plt.show()
    #--------------------------
    cm_lab=['good','bad']
    cm = confusion_matrix(Y_test, predictions)



    #cm.show()

    #print(cm)
    #print Y_test
    #print(predictions)

    #prepare for lm---------------------
    #new_test_set = pandas.DataFrame(columns=['dataset','package','algorithm','nvertices','nedges','nthreads','Nodes.in.largest.WCC','Edges.in.largest.WCC','Nodes.in.largest.SCC','Edges.in.largest.WCC','Average.clustering.coefficient','Number.of.triangles','Fraction.of.closed.triangles','Diameter..longest.shortest.path.','X90.percentile.effective.diameter','classif'])
    new_test_set = pandas.DataFrame(index=data.columns.copy())
    for index, row in data.iterrows():
        if row['classif']== 'good':
            new_test_set=new_test_set.append(row)



    #new_test_set.dropna(axis=1, how='any', inplace=True)
    new_test_set=new_test_set.dropna()
    new_test_set.to_csv('rf_trained.csv',na_rep='NA',index=False)

    global json_data
    json_data={'m': m}
    #json_data=json.dumps(json_data)

    #-----------------------------------------------------------------data prep for django
    

    user_datapoint=X_test.iloc[16]  #random selection for now
    dp_to_render=user_datapoint
    #data.to_sql('learning_set', con=cxn, if_exists='replace')    #learning set
    dp_to_render.to_sql('user_dp', con=cxn, if_exists='replace') #single point in learning set
    
    user_datapoint=user_datapoint.values
    print(user_datapoint)
    user_prediction=classifier.predict(user_datapoint.reshape(1, -1))
    print(user_prediction)




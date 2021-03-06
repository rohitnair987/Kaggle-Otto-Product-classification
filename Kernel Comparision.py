
# coding: utf-8

# In[2]:

import pandas,sklearn
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import *
import random
import numpy as np
from sklearn.feature_selection import SelectFromModel, chi2, f_classif, f_oneway
import matplotlib.pyplot as plt
from sklearn import datasets, svm
from sklearn.feature_selection import SelectPercentile

train1 = pandas.read_csv("D:\\Downloads\\train.csv")
train1 = train1.iloc[np.random.permutation(len(train1))]

def feats(remove):
    f = "feat_"
    ff = []
    f_desc = [34, 11, 25, 60, 14, 3, 27, 62, 46, 40, 36, 67, 26, 69, 54, 61, 39, 8, 80, 90, 88, 28, 50, 75, 42, 15, 24, 76, 20, 9, 86, 38, 4, 59, 58, 57, 17, 82, 2, 43, 68, 72, 41, 53, 64, 45, 49, 18, 23, 32, 70, 79, 35, 19, 33, 85, 92, 7, 22, 66, 83, 71, 13, 29, 37, 91, 55, 73, 78, 48, 47, 56, 21, 30, 44, 81, 87, 1, 10, 31, 52, 77, 16, 5, 89, 84, 74, 93, 63, 65, 51, 12, 6]
    for i in range(len(f_desc) - remove):
        ff.append(f+str(f_desc[i]))
    #print ff
    return ff

folds = 20 #selected after analysis
no_of_features = 76 #selected after analysis

predictors = feats(93 - no_of_features)

for i in predictors:
    train1[i] = train1[i].fillna(train1[i].median())

xtrain = train1[predictors][:20000]
ytrain = train1["target"][:20000]


# In[3]:

scores=[]

for ker in ['linear', 'poly', 'rbf', 'sigmoid']: 
    clf = svm.SVC(kernel=ker)
    score = cross_validation.cross_val_score(clf, xtrain, ytrain, cv=20)
    print(str(ker) + " kernel, accuracy = " + str(score.mean()*100))


# In[ ]:




# In[ ]:




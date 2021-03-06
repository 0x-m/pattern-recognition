# -*- coding: utf-8 -*-
"""Untitled35.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zuEOsz4mPKJT2-PLFR0wgm1fDMZjI91j
"""

import numpy as np
import pandas as pd

#loading datasets------------------------
x_train = pd.read_csv("drive/MyDrive/mnist/Train_Data.csv").to_numpy()
y_train = pd.read_csv("drive/MyDrive/mnist/Train_labels.csv").to_numpy()
x_test = pd.read_csv("drive/MyDrive/mnist/Test_Data.csv").to_numpy()
y_test = pd.read_csv("drive/MyDrive/mnist/Test_labels.csv").to_numpy()
#----------------------------------------

#-------------------top3_Neighbour_points----------------
#returns top 3 nearset points to a given point x among training points 

def top3_Neighbour_points(x_train,y_train,x):
  
  n_samples = x_train.shape[0]

  dists = np.zeros((10,3)) #placeholder for top 3 smallest distances in each of 10 classes
  dists.fill(float('inf')) #fills all dists elements with float infinity (**) (Line 23)

  for i in range(n_samples):
    x_i = x_train[i]
    y_i = int(y_train[i])

    dist = np.linalg.norm(x - x_i)
    if(dists[y_i][2] <= dist): # (**) initial values of dists must be greater than any possible distance ! (Line 17) 
      continue
    else:
      dists[y_i][2] = dist
      if(dists[y_i][1] > dist):
        dists[y_i][1],dists[y_i][2] = dists[y_i][2],dists[y_i][1] #swap
      if(dists[y_i][0] > dist):
        dists[y_i][0],dists[y_i][1] = dists[y_i][1],dists[y_i][0] #swap

  return dists
#----------------------------------------------------------

#--------------------KNN_estimator-------------------------
def KNN_estimator(NNpoints):
  probs = np.zeros((10,3))

  #common constants have been eliminated
  for i in range(10):
    probs[i][0] = 1 / NNpoints[i][0]
    probs[i][1] = 1 / NNpoints[i][1]
    probs[i][2] = 1 / NNpoints[i][2]

  return probs;
#-----------------------------------------------------------

#---------------------bayes_classifier----------------------
#decides based on MAP
def bayes_classifier(probs):
  preds = np.zeros((3,1))
  preds[0][0] = np.argmax(probs[:,0])
  preds[1][0] = np.argmax(probs[:,1])
  preds[2][0] = np.argmax(probs[:,2])

  return preds
#------------------------------------------------------------

#--------------------------evaluate--------------------------
def evaluate(y_pred,y_test):

  n_samples = y_test.shape[0]
  n_corrects = 0

  for i in range(n_samples):
    if(y_pred[i] == y_test[i]):
      n_corrects += 1

  acc = n_corrects / n_samples
  return acc
#------------------------------------------------------------

a = 2
b = 3
print(a,b)
a,b = b,a
print(a,b)

#--------------------PROBLEM #2-----------------------------
n_test_samples = x_test.shape[0]
y_pred = np.zeros((n_test_samples,3))

#loop through all test points---------------
for i in range(n_test_samples):
  top3_dists = top3_Neighbour_points(x_train,y_train,x_test[i]) #find top 3 NN
  probs = KNN_estimator(top3_dists) #computes probabilities based on top 3 NN
  preds = bayes_classifier(probs) #MAP prediction 
  y_pred[i] = preds.reshape((3,)) #accuracy evaluation
#-------------------------------------------

#----------------------------RESULTS-------------------
acck1 = evaluate(y_pred[:,0],y_test)
acck2 = evaluate(y_pred[:,1],y_test)
acck3 = evaluate(y_pred[:,2],y_test)

print("Accuracy for k = 1:\t",acck1,"%")
print("Accuracy for k = 2:\t",acck2,"%")
print("Accuracy for k = 3:\t",acck3,"%")
#------------------------------------------------------
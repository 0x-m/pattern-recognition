# -*- coding: utf-8 -*-
"""Untitled34.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14IEv-n82q7YyqOxqIksy_Fv9fUfOR6OR
"""

import numpy as np
import pandas as pd

#loading datasets------------------------
x_train = pd.read_csv("drive/MyDrive/mnist/Train_Data.csv").to_numpy()
y_train = pd.read_csv("drive/MyDrive/mnist/Train_labels.csv").to_numpy()
x_test = pd.read_csv("drive/MyDrive/mnist/Test_Data.csv").to_numpy()
y_test = pd.read_csv("drive/MyDrive/mnist/Test_labels.csv").to_numpy()
#----------------------------------------

#----------------Rectangular window---------------
def rect_win(x,x_i,h):
  n_features = x.shape[0]
  for i in range(n_features):
    dist = np.abs((x[i] - x_i[i]) / h)
    if(dist > 0.5):
      return 0
  return 1
#-------------------------------------------------

#----------------Gaussian window------------------
#zero mean and unit variance
def gaussian_win(x,x_i,h):
  euclid_dist = np.dot(x - x_i,x - x_i) / (2*h**2)
  exp = np.exp(- euclid_dist)
  exp /= np.pi
  return exp
#-------------------------------------------------

#----------------------Parazen----------------------
#computes p(x|wi)
def parazen_method(x_train,y_train,x,h,window):
  n_samples = x_train.shape[0]
  n_features = x_train.shape[1]
  probs = np.zeros((10,1)) #place holder for p(x|wi)
  
  #V = h** n_features
  for i in range(n_samples):
    x_i = x_train[i]
    y_i = int(y_train[i][0])
    probs[y_i] += window(x_i,x,h) 
  
  return probs
#--------------------------------------------------

#-------------Bayesian Classifier-----------------
# p(wi|x) > p(wj|x) for all i != j --> choose wi
# p(wi|x) = p(x|wi)*p(wi)/p(x)
# assuiming equal prior (p(wi) = 0.1 for (1 <= i <= 10)) then
# bayesian classifier becomes : p(x|wi) > p(x|wj) for all i != j --> choose wi

def bayes_classifier(probs):
  return np.argmax(probs)

#-------------------------------------------------
def evaluate(y_test,y_pred):
  n_samples = y_pred.shape[0]
  n_correct = 0;
  for i in range(n_samples):
    if(y_test[i]== y_pred[i]):
      n_correct += 1

  acc = n_correct / n_samples
  return acc
  #-------------------------------------------------

#---------------------------Problem #1--------------------------------

#helper function---------------
def classify(h,window):
  n_test_samples = x_test.shape[0]

  y_pred = np.zeros((n_test_samples,1))
  for i in range(n_test_samples):
    probs = parazen_method(x_train,y_train,x_test[i],h,window)
    y_pred[i] = bayes_classifier(probs)
  acc = evaluate(y_test,y_pred)
  return acc
#------------------------------

#-------------------------------
#compute accuracy for h = 1.5,1.6,1.7,1.8 and rectangular window
rect_acc = np.zeros((4,1))
rect_acc[0] = classify(1.5,rect_win)
rect_acc[1] = classify(1.6,rect_win)
rect_acc[2] = classify(1.7,rect_win)
rect_acc[3] = classify(1.8,rect_win)
#---------------------------------

#compute accuracy for h = 0.1,0.5,0.6,0.7 and rectangular window
gaus_acc = np.zeros((4,1))
gaus_acc[0] = classify(0.1,gaussian_win)
gaus_acc[1] = classify(0.5,gaussian_win)
gaus_acc[2] = classify(0.6,gaussian_win)
gaus_acc[3] = classify(0.7,gaussian_win)
#---------------------------------

#----------------------------------------------------------------------------

print("Rectangular window with h = 1.5 :")
print(" acc = ",rect_acc[0][0],"%")
print("Rectangular window with h = 1.6 :")
print(" acc = ",rect_acc[1][0],"%")
print("Rectangular window with h = 1.7 :")
print(" acc = ",rect_acc[2][0],"%")
print("Rectangular window with h = 1.8 :")
print(" acc = ",rect_acc[3][0],"%")

print("Gaussian window with h = 0.1 :")
print(" acc = ",gaus_acc[0][0],"%")
print("Gaussian window with h = 0.5 :")
print(" acc = ",gaus_acc[1][0],"%")
print("Gaussian window with h = 0.6 :")
print(" acc = ",gaus_acc[2][0],"%")
print("Gaussian window with h = 0.7 :")
print(" acc = ",gaus_acc[3][0],"%")
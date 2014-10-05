import numpy
import math
import scipy.optimize as opt
from random import randint

from numpy import loadtxt, where, zeros, e, array, log, ones, append, linspace
from pylab import scatter, show, legend, xlabel, ylabel, contour, title
from scipy.optimize import fmin_bfgs

def sigmoid(X):
    return 1 / (1 + numpy.exp(-X))

def cost(theta, X, y):
    p_1 = sigmoid(numpy.dot(X, theta)) # predicted probability of label 1
    log_l = (-y)*numpy.log(p_1) - (1-y)*numpy.log(1-p_1) # log-likelihood vector

    return log_l.mean()

def grad(theta, X, y):
    p_1 = sigmoid(numpy.dot(X, theta))
    error = p_1 - y # difference between label and prediction
    grad = numpy.dot(error, X_1) / y.size # gradient vector
    
    return grad
    
def predict(theta, X, y):
    p_1 = sigmoid(numpy.dot(X, theta))
    return p_1 > 0.5

#
p = predict(array(theta), it)
print 'Train Accuracy: %f' % ((y[where(p == y)].size / float(y.size)) * 100.0)

def trainTheta(theta):
    neutral = open('neutral.csv', 'r')
    push = open('push.csv', 'r')
    
    # Grab data from .csv
    neutralRaw = []
    pushRaw = []
    
    for line in neutral:
        hitComma = False
        temp = ''
        for char in line:
            if (hitComma):
                temp += char
            if (char == ','):
                hitComma = True
        neutralRaw.append(int(temp))
    
    for line in push:
        hitComma = False
        temp = ''
        for char in line:
            if (hitComma):
                temp += char
            if (char == ','):
                hitComma = True
        pushRaw.append(int(temp))

    # Calculate variances
    Xneutral = []
    Xpush = []
    counter = 0
    for i in neutralRaw:
        if (counter >= 9):
            arr = []
            for ii in range(10):
                arr.append(neutralRaw[i-ii])
            Xneutral.append(np.var(arr))
        counter += 1
    
    counter = 0
    for i in pushRaw:
        if (counter >= 9):
            arr = []
            for ii in range(10):
                arr.append(pushRaw[i-ii])
            Xpush.append(np.var(arr))
        counter += 1
    
    # Feature Scaling / Mean Normalization
    #meanNeutral = sum(Xneutral)/float(len(Xneutral))
    #meanPush = sum(Xpush)/float(len(Xpush))
    
    #for i in range(len(Xneutral)):
    #    Xneutral[i] -= meanNeutral
    #for i in range(len(Xpush)):
    #    Xpush[i] -= meanPush
        
    #max(Xneutral)-min(Xneutral)

    
    
    
    # MACHINE LEARNING...
    theta = 50.0 # Chosen by random number generator: KhoKho, guaranteed to be random.
    alpha = .01 # 0.001 <-> 10 Try many.
    
    for i in range(700):     # Arbitrary number of iterations (Gradient Descent)
        sumHypoNeutral = 0.0
        sumHypoPush = 0.0
        for ii in Xneutral:
            sumHypoNeutral += (1.0/(1.0+pow(math.e, -theta*ii)))*ii
        for ii in Xpush:
            sumHypoPush += ((1.0/(1.0+pow(math.e, -theta*ii)))-1.0)*ii
        theta -= alpha*(1.0/(len(Xneutral)+len(Xpush)))*(sumHypoNeutral+sumHypoPush)
        print theta
    
    return theta
    
trainTheta()
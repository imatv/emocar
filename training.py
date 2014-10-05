import numpy as np
import math

def trainTheta():
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
    Xfeatures = []
    counter = 0
    for i in neutralRaw:
        if (counter >= 9):
            arr = []
            for ii in range(10):
                arr.append(neutralRaw[i-ii])
            Xneutral.append(np.var(arr))
            Xfeatures.append(np.var(arr))
        counter += 1
    
    counter = 0
    for i in pushRaw:
        if (counter >= 9):
            arr = []
            for ii in range(10):
                arr.append(pushRaw[i-ii])
            Xpush.append(np.var(arr))
            Xfeatures[1].append(np.var(arr))
        counter += 1
    
    # Feature Scaling / Mean Normalization
    meanNeutral = sum(Xneutral)/float(len(Xneutral))
    meanPush = sum(Xpush)/float(len(Xpush))
    
    for i in range(len(Xneutral)):
        Xneutral[i] -= meanNeutral
    for i in range(len(Xpush)):
        Xpush[i] -= meanPush
        
        
    #max(Xneutral)-min(Xneutral)

    
    
    
    # MACHINE LEARNING...
    theta = 50.0 # Chosen by random number generator: KhoKho, guaranteed to be random.
    alpha = .0001 # 0.001 <-> 10 Try many.
    
    for i in range(7000):     # Arbitrary number of iterations (Gradient Descent)
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
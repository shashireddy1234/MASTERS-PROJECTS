# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:44:20 2021

@author: shash
"""
#we are defining the bias for each connection
import random

#we are defining the weights for each connection
def get_weights(network_size,index):
    #network_size is the number of hidden neurons
    #index is referring to which neuron we are referring to in the layer
    weights=[]
    for i in range(network_size):
        #for empty list of weights we append each of the weights that we read from the user(read the input)
        weights.append(random.random())
#for eg str(index) is str(0) is the 0 th neuron in the layer and str(i) means str(0) is the 0th conncetion of the neuron
    return weights    

    
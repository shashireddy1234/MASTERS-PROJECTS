# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:41:49 2021

@author: shash
"""

from take_inputs import get_weights
import math
import random
#neural network have two inputs and one bias, hidden layer is dynamic(can be any number) that has two neurons one bias value, and output layer has two nerons
class Neuron:
    #assign variables of the class neurons
    #variables will be activationVariable and weights
    #init is to define calling class(self built)
    def __init__(self,activationVariable,num_weights,index):
        self.activationVariable=activationVariable
        self.num_weights=num_weights
        self.gradient=0.0
        
        self.delta=[]
        for i in range(self.num_weights):
            self.delta.append(0.0)
        self.index=index
        self.weights=get_weights(self.num_weights,self.index) #initialising weights 
        #all weights of neurons are being initialised in the start 
        #here we get the weights of the previous layer of that particular neuron and the index of the neuron that we are referring to
    def multweights(self,previousLayer):
            #process where the product of activationVariables and weights take place
            #sigmoid function
            #result is stored as 0 initially
         
        #previousLayer for hidden will be input layer 
         result=0
         for i in range(len(previousLayer)):
            #here we get the weights of the previous layer of that particular neuron and the index of the neuron that we are referring to
            
            if i == 2:
                #since we have two inputs, the last neuron the is bias (0, 1,2) where 0 is the first neuron, 1 is the second neuron and 2 is the bias for that particular  
                #2 is the bias 
                #storing value of bias value (1) and index after multiplying
                #print("result before adding bias =",result,"index =",i)
                #print("result to add=",previousLayer[i].weights[self.index])
                result=result+previousLayer[i].weights[self.index]
                #print("result after adding bias =",result,"index =",i)
                
            else:
                #storing the result of the previous layer 's activation value and index after multiplying using the weights of activation value
                #print("activation value of",i,"=",previousLayer[i].activationVariable)
                #print(previousLayer[i].activationVariable)
                #print("weight =",w[self.index])
                #print(result)
                #print("result before add =",result,"index =",i)
                #print("result to add=",previousLayer[i].activationVariable*previousLayer[i].weights[self.index])
                #print("split of result to add=","activation variable of prev layer",i,":",previousLayer[i].activationVariable,"*","weight number",self.index,":",previousLayer[i].weights[self.index])
                result=result+(previousLayer[i].activationVariable*previousLayer[i].weights[self.index])
                #print("result after add =",result,"index =",i)
         #print("final  result =",result)       
         activation=1/(1+math.exp(-(result)))      #to calculate sigmoid function
         return activation
    #it returns the value of activation function 
    
    
                
                
                
                
                
                
           

                
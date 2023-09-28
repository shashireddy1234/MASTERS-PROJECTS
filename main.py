6# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:08:13 2021

@author: shash
"""
import math
from class_Neuron import Neuron
import pandas as pd





data_train=pd.read_csv("training.csv",names=["x","y","v1","v2"])
data=data_train.values[:,:2]
output=data_train.values[:,2:]



data_val=pd.read_csv("testing.csv",names=["x","y","v1","v2"])
val_input=data_val.values[:,:2]
val_output=data_val.values[:,2:]
#xor data
input_layer=[Neuron(0,2,0),Neuron(0,2,1),Neuron(0,2,2)]
#in input layer,first is the activation value which is the initial value and it should be updates in the feedforward process
#second is the number of weights that will define number of nodes in the next layer
#third is the index number which tells which row we are referring to
hidden_layer=[Neuron(0,2,0),Neuron(0,2,1),Neuron(0,2,2)]
output_layer=[Neuron(0, 0, 0),Neuron(0,0,1)]

predicted_value=[]


lambdaValue=0.5

momentum=0.2

learning_rate=0.3

def feedforward(input_data):
    #using the input data that we gave first
    
    for i in range(len(input_layer)):
        #i is the bias value in which the activation value is 1 and for neurons except bias, we take the values from the input_data
        if i==2:
            input_layer[i].activationVariable=1 #it is 1 as it is the bias value
        else:
            
            input_layer[i].activationVariable=input_data[i] # if not bias value we take value from the input_data
    
    
    for i in range(len(hidden_layer)):
        # for hidden layer if activation value is 2, then it is bias 
        if i==2:
            hidden_layer[i].activationVariable=1 # the activation value for bias is 1
        else:
            hidden_layer[i].activationVariable=hidden_layer[i].multweights(input_layer)#for hidden layer activation values, we take the weights and activation values of the input nerons and multiply to get the activation values for hidden layer
        #print("activation value of hidden layer",i,"=",hidden_layer[i].activationVariable)
    for i in range(len(output_layer)):
    # there will be no if statements as we do not have bias in the output_layer,so we take the activation value and the weights of the hidden layer and multiply to get the activation value for output layer
        output_layer[i].activationVariable=output_layer[i].multweights(hidden_layer)
        predicted_value.append(output_layer[i].activationVariable)
        
        #print("act val of output",i,"=",output_layer[i].activationVariable)
        






def backpropagation(output):
    error=[]#intialise error
    for i in range(len(output_layer)):
        error.append(output[i]-output_layer[i].activationVariable)#calculating two error values for output
    #calculate error[0] and error[1]
    
    
    for i in range(len(output_layer)): #updating the gradient of output layer
    #we use the gradient of the output layer to calc the  delta weights of hidden layer
        #print("first grad val of output layer",i,"=",output_layer[i].gradient)
        #print("error in grad val",i,"=",error[i])
        output_layer[i].gradient=lambdaValue*output_layer[i].activationVariable*(1-output_layer[i].activationVariable)*error[i]
        #print("Output_layer",i,"gradient =",output_layer[i].gradient)
     #local_grad_output=lambda*output_layer[0].activationVariable*(1-output_layer[0].activationVariable)*error[0]
     #local_grad_output=lambda*output_layer[1].activationVariable*(1-output_layer[1].activationVariable)*error[1]
        
    for i in range(len(hidden_layer)):#updating gradient of hidden layer
         temp=0
         for j in range(len(output_layer)):
             temp+=output_layer[j].gradient*hidden_layer[i].weights[j]
         hidden_layer[i].gradient=lambdaValue*hidden_layer[i].activationVariable*(1-hidden_layer[i].activationVariable)*temp
         
    for i in range(len(hidden_layer)):
        for j in range(len(output_layer)):
            #print("first delta weight of hidden layer",i,"delta weight",j,"=",hidden_layer[i].delta[j])
            #print("splittin delta::::::","output layer ",j,"gradient value=",output_layer[j].gradient,"     ","hidden layer",i,"activation =",hidden_layer[i].activationVariable)
            
            hidden_layer[i].delta[j]=(learning_rate*output_layer[j].gradient*hidden_layer[i].activationVariable)+momentum*hidden_layer[i].delta[j]
            #print("hidden layer",i,"delta weights",j,"=",hidden_layer[i].delta[j])
            
    for i in range(len(input_layer)):
        for j in range(len(hidden_layer)-1):
            input_layer[i].delta[j]=learning_rate*hidden_layer[j].gradient*input_layer[i].activationVariable+momentum*input_layer[i].delta[j]
            
    for i in range(len(hidden_layer)):#updated weights
        for j in range(len(output_layer)):
            hidden_layer[i].weights[j]=hidden_layer[i].weights[j]+hidden_layer[i].delta[j]
            #print("hidden layer",i,"weights",j,"=",hidden_layer[i].weights[j])
            
    for i in range(len(input_layer)):
        for j in range(len(hidden_layer)-1):
            input_layer[i].weights[j]=input_layer[i].weights[j]+input_layer[i].delta[j]
            
    for i in range(len(error)):#squaring each errors
        error[i]=(error[i])**2
        
    mean_squared_error=sum(error)/len(error)
    
    return mean_squared_error



       
epoch=0 
rmse=[]
val_error=[]  
mean_squared_error_validation=[]
for i in range(1000):
    epoch=epoch+1
    print(epoch)
    
    for i in range(len(data)):
        #print("input data=",data[i])
        feedforward(data[i])
        rmse.append(backpropagation(output[i]))
        #print("rmse =",rmse)
        
    root_mean_squared=math.sqrt(sum(rmse)/len(rmse))

    print("root mean square =",root_mean_squared)
    
    for i in range(len(val_input)):
        feedforward(val_input[i])
        for j in range(len(output_layer)):
            error=(val_output[i][j]-output_layer[j].activationVariable)**2
            val_error.append(error)
            
        mean_squared_error_validation.append(sum(val_error)/len(val_error))
        
    root_mean_square_validation=math.sqrt(sum(mean_squared_error_validation)/len(mean_squared_error_validation))
    
    
    print("root mean square validation =",root_mean_square_validation)
            
        
            


input_weights=[]
for i in range(len(input_layer)):
    
    input_weights.append(input_layer[i].weights)
hidden_weights=[]   
for i in range(len(hidden_layer)):
    hidden_weights.append(hidden_layer[i].weights)
    

    
    
weights=pd.DataFrame({'input weights':input_weights,'hidden weights':hidden_weights})
weights.to_csv(path_or_buf="weights",index=False)  
    
         
         
     
    
    
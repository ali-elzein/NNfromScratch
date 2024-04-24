import sys
import numpy as np
import matplotlib

def neuron_output(weights, inputs, bias):
    output = 0
    for i in range(len(inputs)):
        output += inputs[i] * weights[i]
    return output + bias
    

inputs = [1, 2, 3, 2.5] # output from 3 neurons in prev layer
weights1 = [0.2, 0.8, -0.5, 1.0] # weight for each input into neuron1
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2 # bias used to calc output from neuron1
bias2 = 3
bias3 = 0.5

# calculated output for the 3 neurons in the layer
layer_output = [neuron_output(inputs, weights1, bias1),
                neuron_output(inputs, weights2, bias2),
                neuron_output(inputs, weights3, bias3)]

print(layer_output) # output of neuron1
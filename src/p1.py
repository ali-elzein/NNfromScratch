import sys
import numpy as np
import matplotlib

inputs = [1, 2, 3, 2.5] # output from 3 neurons in prev layer

weights1 = [0.2, 0.8, -0.5, 1.0] # weight for each input into neuron1
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
weights = [weights1, weights2, weights3]

bias1 = 2 # bias used to calc output from neuron1
bias2 = 3
bias3 = 0.5
biases = [bias1, bias2, bias3]

layer_output = np.dot(weights, inputs) + biases # calculated output for the 3 neurons in the layer
print(layer_output)
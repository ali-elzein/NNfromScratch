import sys
import numpy as np
import matplotlib

# batch size is the # of inputs taken at once
# output from 3 neurons in prev layer
inputs = [[1, 2, 3, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

weights1 = [0.2, 0.8, -0.5, 1.0] # weight for each input into neuron1
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
weights = [weights1, weights2, weights3]

bias1 = 2 # bias used to calc output from neuron1
bias2 = 3
bias3 = 0.5
biases = [bias1, bias2, bias3]

# now that inputs are a matrix and not just an array, matrix mult will be performed
# to make the # of rows in weights (3) match the cols in inputs (4), transpose weights
layer_output = np.dot(inputs, np.array(weights).T) + biases # calculated output for the 3 neurons in the layer
print(layer_output)
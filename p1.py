import sys
import numpy as np
import matplotlib

inputs = [1.2, 5.1, 2.1] # output from 3 neurons in prev layer
weights = [3.1, 2.1, 8.7] # weight for each input
bias = 3

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias # neuron output
print(output)
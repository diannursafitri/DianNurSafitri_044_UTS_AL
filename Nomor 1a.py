import numpy as np

inputs = [4.0, 5.0, 2.1, 4.3, 4.5, 4.3, 3.5, 7.5, 3.4, 6.5]
weights = [3.2, 1.2, 4.3, 0.6, 1.5, 6.2, 2.4, 3.2, 1.5, 3.4]

bias = 5.5

outputs = np.dot(weights, inputs) + bias
print(outputs)

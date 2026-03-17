import numpy as np
ones_array = np.ones((2, 3)) 
zeros_array = np.zeros((2, 
3)) 
empty_array = np.empty((2, 
3)) 
print("Ones:\n", ones_array) 
print("Zeros:\n", 
zeros_array) 
print("Empty:\n", 
empty_array) 
arr = np.array([[1, 2, 3], [4, 
5, 6]]) 
print("Shape of array:", 
arr.shape) 
reshaped = arr.reshape(3, 2) 
print("Reshaped array:\n", 
reshaped)
import numpy as np

# Create two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication using dot()
result = np.dot(A, B)

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Result using dot():")
print(result)
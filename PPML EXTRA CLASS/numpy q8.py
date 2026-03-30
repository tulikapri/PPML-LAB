import numpy as np

# Create an array
arr = np.array([50, 20, 40, 10, 30])

# Ascending order
asc = np.sort(arr)

# Descending order
desc = np.sort(arr)[::-1]

print("Original Array:", arr)
print("Ascending Order:", asc)
print("Descending Order:", desc)
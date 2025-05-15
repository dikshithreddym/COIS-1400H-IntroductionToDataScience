#Dikshith Reddy M
#0789055

import numpy as np

# Create a one-dimensional array with 1000 random numbers between 1 and 100
myArray = np.random.randint(1, 101, size=1000)

# Print shape and datatype of the array
print(f"Shape of the array: {myArray.shape}")
print(f"Datatype of the array: {myArray.dtype}")

# Print min, max, sum, mean, and standard deviation of the array
print(f"Minimum value: {np.min(myArray)}")
print(f"Maximum value: {np.max(myArray)}")
print(f"Sum of all values: {np.sum(myArray)}")
print(f"Mean of the values: {np.mean(myArray)}")
print(f"Standard Deviation: {np.std(myArray)}")

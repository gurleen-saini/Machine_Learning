import numpy as np

# Create a 1D array
one_d_array = np.array([1, 2, 3, 4])
print("1D Array:")
print(one_d_array)

# Create a 2D array
two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(two_d_array)

# Check the type of one_d_array
print("\nType of one_d_array:")
print(type(one_d_array))

# Find the dimension of one_d_array
print("\nDimension of one_d_array:")
print(one_d_array.ndim)

# Find the size of one_d_array
print("\nSize of one_d_array:")
print(one_d_array.size)

# Find the shape of two_d_array
print("\nShape of two_d_array:")
print(two_d_array.shape)

# Find the data type of one_d_array
print("\nData type of one_d_array:")
print(one_d_array.dtype)

# Create a 3x3 array of ones
print("\n3x3 Array of Ones:")
print(np.ones((3, 3), dtype=int))

# Create a 3x3 array of zeros
print("\n3x3 Array of Zeros:")
print(np.zeros((3, 3), dtype=int))

# Create an empty 2x4 array
print("\nEmpty 2x4 Array:")
print(np.empty((2, 4)))

# Create an array with values from 1 to 12
arr = np.arange(1, 13)
print("\nArray with values from 1 to 12:")
print(arr)

# Create an array with 4 linearly spaced values between 1 and 5
print("\nArray with 4 linearly spaced values between 1 and 5:")
print(np.linspace(1, 5, 4))

# Reshape arr to a 3x4 array
arr_reshape = np.reshape(arr, (3, 4))
print("\nReshaped Array (3x4):")
print(arr_reshape)

# Flatten the reshaped array
print("\nFlattened Array:")
print(arr_reshape.flatten())

# Create a 1D array
one_d_array = np.array([1, 2, 3, 4])
print("1D Array:")
print(one_d_array)  # Printing 1D array

# Create a 2D array
two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(two_d_array)  # Printing 2D array

# Give the type of data present in one_d_array variable
print("\nType of one_d_array:")
print(type(one_d_array))

# Find the dimension of one_d_array
print("\nDimension of one_d_array:")
print(one_d_array.ndim)

# Find the size of one_d_array
print("\nSize of one_d_array:")
print(one_d_array.size)

# Find the shape of two_d_array
print("\nShape of two_d_array:")
print(two_d_array.shape)

# Find the data type of one_d_array
print("\nData type of one_d_array:")
print(one_d_array.dtype)

# Create a 3x3 array of ones
print("\n3x3 Array of Ones:")
print(np.ones((3, 3), dtype=int))

# Create a 3x3 array of zeros
print("\n3x3 Array of Zeros:")
print(np.zeros((3, 3), dtype=int))

# Create an empty 2x4 array
print("\nEmpty 2x4 Array:")
print(np.empty((2, 4)))

# Create an array with values from 1 to 12
arr = np.arange(1, 13)
print("\nArray with values from 1 to 12:")
print(arr)

# Create an array with 4 linearly spaced values between 1 and 5
print("\nArray with 4 linearly spaced values between 1 and 5:")
print(np.linspace(1, 5, 4))

# Reshape arr to a 3x4 array
arr_reshape = np.reshape(arr, (3, 4))
print("\nReshaped Array (3x4):")
print(arr_reshape)

# Flatten the reshaped array
print("\nFlattened Array:")
print(arr_reshape.flatten())

print(np.ones((3, 3), dtype=int))
print(np.zeros((3, 3), dtype=int))
print(np.empty((2, 4)))
arr = np.arange(1, 13)
print(arr)
print(np.linspace(1, 5, 4))
arr_reshape = np.reshape(arr, (3, 4))
print(arr_reshape)
print(arr_reshape.flatten())


sin_90 = np.sin(90) # sine value of degree 90 in degree
print("Sine value of angle 90 in degree = ",sin_90) # print sine value

sin_90 = np.sin(90 * np.pi/180) # sine value of angle 90 in radinas
print("Sine value of angle 90 in radians = ", sin_90)

cos_180 = np.cos(180) # cosine value of degree 180 in degree
print("Cosine value of angle 180 in degree = ", cos_180) # print cosine value

cos_180 = np.cos(180 * np.pi/180)
print("Cosine value of angle 180 in radians = ", cos_180)

tan_60 = np.tan(60) # tangent value of degree 60 in degree
print("Tangent value of angle 60 in degree = ", tan_60) # print tangent value

tan_60 = np.tan(60 * np.pi/180) # tangent value of degree 60 in degree
print("Tangent value of angle 60 in radians = ", tan_60) # print tangent value

# Create two 3x3 arrays
arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.arange(1, 10).reshape(3, 3)

# Print arr1 and arr2
print("Array 1:")
print(arr1)
print("\nArray 2:")
print(arr2)

# Add arrays
print("\nAddition (arr1 + arr2):")
print(arr1 + arr2)

print("\nAddition using np.add(arr1, arr2):")
print(np.add(arr1, arr2))

# Subtract arrays
print("\nSubtraction (arr1 - arr2):")
print(arr1 - arr2)

print("\nSubtraction using np.subtract(arr1, arr2):")
print(np.subtract(arr1, arr2))

# Divide arrays
print("\nDivision (arr1 / arr2):")
print(arr1 / arr2)

print("\nDivision using np.divide(arr1, arr2):")
print(np.divide(arr1, arr2))

# Multiply arrays
print("\nMultiplication (arr1 * arr2):")
print(arr1 * arr2)

print("\nMultiplication using np.multiply(arr1, arr2):")
print(np.multiply(arr1, arr2))

# Matrix multiplication
print("\nMatrix Multiplication (arr1 @ arr2):")
print(arr1 @ arr2)

print("\nMatrix Multiplication using arr1.dot(arr2):")
print(arr1.dot(arr2))

# Maximum value in arr1
print("\nMaximum value in arr1:")
print(arr1.max())

print("\nMaximum value in each column of arr1 (axis=0):")
print(arr1.max(axis=0))

print("\nMaximum value in each row of arr1 (axis=1):")
print(arr1.max(axis=1))

# Index of the maximum value in arr1
print("\nIndex of maximum value in arr1:")
print(arr1.argmax())

# Minimum value in arr1
print("\nMinimum value in arr1:")
print(arr1.min())

print("\nMinimum value in each column of arr1 (axis=0):")
print(arr1.min(axis=0))

# Index of the minimum value in arr1
print("\nIndex of minimum value in arr1:")
print(arr1.argmin())

# Sum of all elements in arr1
print("\nSum of all elements in arr1:")
print(np.sum(arr1))

print("\nSum of each column in arr1 (axis=0):")
print(np.sum(arr1, axis=0))

# Mean of all elements in arr1
print("\nMean of all elements in arr1:")
print(np.mean(arr1))

# Square root of all elements in arr1
print("\nSquare root of all elements in arr1:")
print(np.sqrt(arr1))

# Standard deviation of all elements in arr1
print("\nStandard deviation of all elements in arr1:")
print(np.std(arr1))

# Exponential of all elements in arr1
print("\nExponential of all elements in arr1:")
print(np.exp(arr1))

# Natural logarithm of all elements in arr1
print("\nNatural logarithm of all elements in arr1:")
print(np.log(arr1))

# Base-10 logarithm of all elements in arr1
print("\nBase-10 logarithm of all elements in arr1:")
print(np.log10(arr1))

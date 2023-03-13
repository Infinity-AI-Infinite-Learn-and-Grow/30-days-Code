# First, install numpy on your system Create Numpy array and also create Multidimensional Array. Numpy array converts into a list.
# Also perform Addition (+),Subtraction (-),Multiplication (x),Division (/),Modules (%),Floor Division(//), Exponential(**) operation with numpy.
# Note: If any queries Please ask in a group.


# --Task 1--

# pip install numpy --> for installing
import numpy as np

# Create a 1-dimensional Numpy array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Create a 2-dimensional Numpy array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Convert the Numpy array to a list
arr_list = arr1.tolist()

# Print the list
print(arr_list)


# -- Task 2--

# Create two Numpy arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Addition
c = a + b
print(c)  # Output: [5 7 9]

# Subtraction
c = a - b
print(c)  # Output: [-3 -3 -3]

# Multiplication
c = a * b
print(c)  # Output: [ 4 10 18]

# Division
c = b / a
print(c)  # Output: [4.  2.5 2. ]

# Modules
c = b % a
print(c)  # Output: [0 1 0]

# Floor Division
c = b // a
print(c)  # Output: [4 2 2]

# Exponential
c = a ** 2
print(c)  # Output: [1 4 9]

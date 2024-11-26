# Import NumPy library
import numpy as np

# Create two NumPy arrays
array1 = np.array([1, 4, 9, 16, 25])
array2 = np.array([5, 10, 15, 20, 25])

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

# Perform element-wise operations
addition = np.add(array1, array2)
subtraction = np.subtract(array1, array2)
multiplication = np.multiply(array1, array2)
division = np.divide(array1, array2)

print("\nElement-wise Addition:")
print(addition)

print("\nElement-wise Subtraction:")
print(subtraction)

print("\nElement-wise Multiplication:")
print(multiplication)

print("\nElement-wise Division:")
print(division)

# Universal functions
sqrt_array1 = np.sqrt(array1)
log_array1 = np.log(array1)  # Natural logarithm (base e)
exp_array1 = np.exp(array1)

print("\nSquare Root of Array 1:")
print(sqrt_array1)

print("\nNatural Logarithm (ln) of Array 1:")
print(log_array1)

print("\nExponential (e^x) of Array 1:")
print(exp_array1)

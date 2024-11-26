# Prerequisite: Install NumPy
# Run the following command in your terminal or command prompt to install NumPy:
# pip install numpy

import numpy as np

# Create arrays using lists
list_array = np.array([1, 2, 3, 4, 5])
print("Array created from a list:")
print(list_array)
print(f"Attributes: Shape={list_array.shape}, Data Type={list_array.dtype}, Size={list_array.size}, Dimensions={list_array.ndim}\n")

# Create arrays using built-in functions
zeros_array = np.zeros((2, 3))
print("Array of zeros:")
print(zeros_array)
print(f"Attributes: Shape={zeros_array.shape}, Data Type={zeros_array.dtype}, Size={zeros_array.size}, Dimensions={zeros_array.ndim}\n")

ones_array = np.ones((3, 2), dtype=int)
print("Array of ones:")
print(ones_array)
print(f"Attributes: Shape={ones_array.shape}, Data Type={ones_array.dtype}, Size={ones_array.size}, Dimensions={ones_array.ndim}\n")

arange_array = np.arange(0, 10, 2)
print("Array created with arange:")
print(arange_array)
print(f"Attributes: Shape={arange_array.shape}, Data Type={arange_array.dtype}, Size={arange_array.size}, Dimensions={arange_array.ndim}\n")

random_array = np.random.rand(2, 2)
print("Randomly generated array:")
print(random_array)
print(f"Attributes: Shape={random_array.shape}, Data Type={random_array.dtype}, Size={random_array.size}, Dimensions={random_array.ndim}")

# Import NumPy library
import numpy as np

# Create a 1D NumPy array
original_array = np.arange(1, 13)
print("Original Array (1D):")
print(original_array)
print(f"Shape: {original_array.shape}, Dimensions: {original_array.ndim}\n")

# Reshape the array into 2D (3x4)
reshaped_2d = original_array.reshape(3, 4)
print("Reshaped Array (2D - 3x4):")
print(reshaped_2d)
print(f"Shape: {reshaped_2d.shape}, Dimensions: {reshaped_2d.ndim}\n")

# Reshape the array into 3D (2x2x3)
reshaped_3d = original_array.reshape(2, 2, 3)
print("Reshaped Array (3D - 2x2x3):")
print(reshaped_3d)
print(f"Shape: {reshaped_3d.shape}, Dimensions: {reshaped_3d.ndim}\n")

# Transpose the 2D array
transposed_2d = reshaped_2d.T
print("Transpose of the Reshaped 2D Array:")
print(transposed_2d)
print(f"Shape: {transposed_2d.shape}, Dimensions: {transposed_2d.ndim}\n")

# Swap axes of the 3D array (swap axes 0 and 2)
swapped_axes = reshaped_3d.swapaxes(0, 2)
print("3D Array with Swapped Axes (0 and 2):")
print(swapped_axes)
print(f"Shape: {swapped_axes.shape}, Dimensions: {swapped_axes.ndim}")

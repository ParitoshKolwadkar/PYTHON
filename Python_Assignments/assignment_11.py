# Import NumPy
import numpy as np

# Create a 2D NumPy array
array = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Original Array:")
print(array)

# 1. Accessing specific elements
print("\nAccess specific element [1,2] (row 1, column 2):", array[1, 2])  # 70

# 2. Accessing entire rows and columns
print("\nAccess row 0:", array[0])  # [10, 20, 30, 40]
print("Access column 2:", array[:, 2])  # [30, 70, 110]

# 3. Slicing operations
print("\nSlicing rows 0 to 1 and columns 1 to 3:")
print(array[0:2, 1:3])  # Subarray [[20, 30], [60, 70]]

# 4. Boolean indexing
print("\nBoolean indexing (elements > 50):")
print(array[array > 50])  # [60, 70, 80, 90, 100, 110, 120]

# 5. Fancy indexing
print("\nFancy indexing (specific rows and columns):")
rows = [0, 2]  # First and last rows
columns = [1, 3]  # Second and last columns
print(array[np.ix_(rows, columns)])  # Subarray [[20, 40], [100, 120]]

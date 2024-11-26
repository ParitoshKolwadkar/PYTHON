import numpy as np

# Create a sample 2D NumPy array
array = np.array([[10, 20, 30, 40],
                  [50, 60, 70, 80],
                  [90, 100, 110, 120]])

print("Original Array:")
print(array)

# 1. Accessing Specific Elements
# Access element at row 1, column 2 (indexing starts from 0)
element = array[1, 2]
print("\nElement at row 1, column 2:", element)

# 2. Accessing Entire Rows and Columns
# Access all elements of row 0
row_0 = array[0, :]
print("\nRow 0:", row_0)

# Access all elements of column 2
col_2 = array[:, 2]
print("\nColumn 2:", col_2)

# 3. Slicing Operations (Extracting Subarrays)
# Extract a subarray of rows 0 to 1 and columns 1 to 2
subarray = array[0:2, 1:3]
print("\nSubarray (rows 0-1, columns 1-2):")
print(subarray)

# 4. Boolean Indexing (Filtering based on conditions)
# Create a boolean mask where we want values greater than 60
mask = array > 60
print("\nBoolean Mask (values > 60):")
print(mask)

# Use the mask to extract values greater than 60
filtered_values = array[mask]
print("\nFiltered Values (greater than 60):")
print(filtered_values)

# 5. Fancy Indexing (Selecting Specific Rows and Columns)
# Select rows 0 and 2, and columns 1 and 3
fancy_indexed = array[[1, 2], [0,2]]
print("\nFancy Indexing (Element at row 1, column 0 and row 2, column 2):")
print(fancy_indexed)

# 6. Modifying Elements Using Indexing
# Change the element at row 1, column 1 to 999
array[1, 1] = 999
print("\nModified Array (element at row 1, column 1 changed to 999):")
print(array)

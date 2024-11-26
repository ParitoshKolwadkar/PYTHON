# Import Pandas
import pandas as pd

# Create a dictionary of lists
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 28],
    "Score": [85, 90, 95, 88, 92]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Display the last few rows of the DataFrame
print("\nLast few rows of the DataFrame:")
print(df.tail())

# Display information about the DataFrame
print("\nDataFrame Information:")
print(df.info())

# Display basic statistics for numerical columns
print("\nBasic Statistics:")
print(df.describe())

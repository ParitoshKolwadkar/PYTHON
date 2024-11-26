# Import Pandas
import pandas as pd

# Read data from a CSV file
# Replace 'data.csv' with the path to your CSV file
df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Display information about the DataFrame
print("\nDataFrame Information:")
print(df.info())

# Display basic statistics for numerical columns
print("\nBasic Statistics:")
print(df.describe())

# Modify the DataFrame (example: adding a new column)
df['NewColumn'] = 'SampleData'

# Save the modified DataFrame to a new CSV file
df.to_csv('modified_data.csv', index=False)
print("\nModified DataFrame has been saved to 'modified_data.csv'.")

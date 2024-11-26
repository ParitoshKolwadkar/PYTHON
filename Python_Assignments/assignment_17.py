# Import Pandas
import pandas as pd
import numpy as np

# Sample data with missing values
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, np.nan, 35, 40, np.nan],
    "Salary": [50000, 60000, np.nan, 70000, 65000],
    "Bonus": [5000, np.nan, 5500, 7000, 5200]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame with Missing Values:")
print(df)

# Handle missing values:
# Option 1: Fill missing values with a specific value (e.g., 0 or mean)
df_filled = df.fillna({"Age": df["Age"].mean(), "Salary": df["Salary"].mean(), "Bonus": 0})

# Option 2: Drop rows with any missing values
df_dropped = df.dropna()

# Perform aggregation operations on columns
age_mean = df_filled["Age"].mean()
salary_sum = df_filled["Salary"].sum()
bonus_mean = df_filled["Bonus"].mean()

# Display the results
print("\nDataFrame after Filling Missing Values:")
print(df_filled)

print("\nDataFrame after Dropping Rows with Missing Values:")
print(df_dropped)

print("\nAggregation Results:")
print(f"Mean Age: {age_mean}")
print(f"Total Salary: {salary_sum}")
print(f"Mean Bonus: {bonus_mean}")

# Import Pandas
import pandas as pd

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 28],
    "Salary": [50000, 60000, 55000, 70000, 65000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Filter rows where Age > 30 using Boolean indexing
filtered_df_boolean = df[df["Age"] > 30]

# Filter rows where Age > 30 using the query() method
filtered_df_query = df.query("Age > 30")

# Sort the filtered DataFrame by the 'Salary' column in descending order
sorted_df = filtered_df_boolean.sort_values(by="Salary", ascending=False)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Display the filtered DataFrame (Boolean indexing)
print("\nFiltered DataFrame (Age > 30, Boolean indexing):")
print(filtered_df_boolean)

# Display the filtered DataFrame (query() method)
print("\nFiltered DataFrame (Age > 30, query() method):")
print(filtered_df_query)

# Display the sorted DataFrame
print("\nSorted DataFrame (Filtered rows sorted by Salary in descending order):")
print(sorted_df)

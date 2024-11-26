# Import Pandas
import pandas as pd

# Sample data
data = {
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance", "HR"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
    "Salary": [50000, 60000, 55000, 70000, 65000, 80000, 52000],
    "Bonus": [5000, 6000, 5500, 7000, 6500, 8000, 5200]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group data by the 'Department' column
grouped = df.groupby("Department")

# Compute aggregate statistics
salary_stats = grouped["Salary"].agg(["sum", "mean"])
bonus_stats = grouped["Bonus"].agg(["sum", "mean"])

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Display salary statistics
print("\nSalary Statistics by Department:")
print(salary_stats)

# Display bonus statistics
print("\nBonus Statistics by Department:")
print(bonus_stats)

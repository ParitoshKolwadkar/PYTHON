# Import NumPy
import numpy as np

# Create a 1D NumPy array
array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:")
print(array)

# Statistical computations
mean_value = np.mean(array)
median_value = np.median(array)
std_deviation = np.std(array)
variance_value = np.var(array)

print("\nStatistical Computations:")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_deviation}")
print(f"Variance: {variance_value}")

# Advanced statistical methods
percentile_25 = np.percentile(array, 25)  # 25th percentile
percentile_50 = np.percentile(array, 50)  # Median
percentile_75 = np.percentile(array, 75)  # 75th percentile

print("\nPercentiles:")
print(f"25th Percentile: {percentile_25}")
print(f"50th Percentile (Median): {percentile_50}")
print(f"75th Percentile: {percentile_75}")

# Create another array for correlation computation
array2 = np.array([15, 25, 35, 45, 55, 65, 75, 85, 95, 105])

# Compute correlation coefficient
correlation_matrix = np.corrcoef(array, array2)

print("\nCorrelation Coefficient Matrix:")
print(correlation_matrix)

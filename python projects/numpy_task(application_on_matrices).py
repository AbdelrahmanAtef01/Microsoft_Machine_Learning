import numpy as np

# 1- Creating a dataset using `arange` and `reshape`
data = np.arange(1, 21).reshape((4, 5))
print("Original Data:\n", data)

# 2- Scaling the data
scaled_data = data * 10
print("\nScaled Data (multiplied by 10):\n", scaled_data)

# 3- Extract a sub-matrix
sub_matrix = scaled_data[1:3, 2:5]
print("\nSub-matrix (rows 1 to 2, columns 2 to 4):\n", sub_matrix)

# 4- Calculate sum, mean, and standard deviation
total_sum = np.sum(scaled_data)
mean_value = np.mean(scaled_data)
std_dev = np.std(scaled_data)
print("\nSome values from the data :\n")
print("Total Sum:", total_sum)
print("Mean:", mean_value)
print("Standard Deviation:", std_dev)

# 5- Square the elements
squared_data = np.power(scaled_data, 2)
print("\nSquared Data:\n", squared_data)

# 6- Broadcasting: Add a constant vector to each row
constant_vector = np.array([1, 2, 3, 4, 5])
broadcasted_data = scaled_data + constant_vector
print("\nBroadcasted Data (added [1, 2, 3, 4, 5] to each row):\n", broadcasted_data)

# 7- Matrix multiplication and inverse

# Creating another matrix for multiplication
matrix_b = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
result_matrix = np.dot(scaled_data, matrix_b)
print("\nMatrix Multiplication Result:\n", result_matrix)

# For matrix inversion, we need a square matrix
square_matrix = np.array([[1, 2], [3, 4]])
inverse_matrix = np.linalg.inv(square_matrix)
print("\nInverse of the square matrix [[1, 2], [3, 4]]:\n", inverse_matrix)

# 8- Combine some of the used methods to get the standard deviation
standard_deviation = np.sqrt(np.sum(np.square(broadcasted_data - np.mean(broadcasted_data)))/np.size(broadcasted_data))
print("\nStandard deviation equation Result:", standard_deviation)
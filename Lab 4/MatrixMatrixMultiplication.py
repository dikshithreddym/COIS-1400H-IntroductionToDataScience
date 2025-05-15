"""

Dikshith Reddy M
0789055

Lab 4 - Profiling Python Code for Matrix Multiplication

The goal of this lab is to investigate methods for profiling Python code. We focus on profiling a script that performs matrix multiplication. This script multiplies two square matrices of the same size, where the size is specified by the user.

Part 1: We added runtime measurements to observe the time needed for computation per element.
    The analysis revealed that the runtime increases cubically as the size of the matrices increases, demonstrating the O(n^3) complexity of the nested loop multiplication algorithm.
    This highlights the importance of optimizing algorithmic efficiency for large-scale computations.

Part 2: By adding the @profile decorator for memory profiling, we introduced an overhead that slightly increased the runtimes for the lower half of the tested matrix sizes.
    This profiling provided valuable insights into the memory usage of the function, crucial for optimizing memory consumption in data-intensive applications. The increase in runtime with profiling enabled underscores the trade-off between obtaining detailed performance metrics and the execution speed of the code.

Usage:
    - Run this script and enter the desired size of the matrices when prompted.
    - The script outputs the overall time taken for the multiplication, the number of elements in the result matrix, and the time taken per element in milliseconds.

Note:
    This script requires the memory_profiler package for memory usage profiling.
"""

import random
import time
from memory_profiler import profile

@profile
def multiply():
    for i in range(size):
        for j in range(size):
            for k in range(size):
                P[i][j] = P[i][j] + (A[i][k] * B[k][j])  # Multiplication operation

size = int(input("Enter size: "))

r1, c1, r2, c2 = size, size, size, size

# Initialize matrices A and B with random numbers and P with zeros
A = [[random.randint(1, 100) for _ in range(c1)] for _ in range(r1)]
B = [[random.randint(1, 100) for _ in range(c2)] for _ in range(r2)]
P = [[0 for _ in range(c2)] for _ in range(r1)]

# Start timer
start_time = time.time()

multiply()

# Stop timer
end_time = time.time()

# Compute elapsed time
elapsed_time = end_time - start_time

# Compute number of elements in the result matrix
num_elements = size * size  # Total number of elements in the result matrix
# Compute time per element in milliseconds
time_per_element = (elapsed_time / num_elements) * 1000  # Time per element in milliseconds

# Print overall time, number of elements, and time per element
print(f"Overall time: {elapsed_time:.4f}s")
print(f"Number of elements in the result matrix: {num_elements}")
print(f"Time per element: {time_per_element:.4f}ms")

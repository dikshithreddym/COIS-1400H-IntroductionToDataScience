#Dikshith Reddy M
#0789055

'''
Observations on Sorting Algorithm Runtimes:
- As the size of the array increases, the time it takes for all sorting algorithms to complete also increases.
- Quicksort tends to be very fast in many cases but can degrade in performance in worst-case scenarios.
- Mergesort provides a stable sort and its performance is more predictable across different datasets, but it tends to be slightly slower than Quicksort on average.
- Heapsort shows consistent performance regardless of the initial order of the data, but it is generally slower than both Quicksort and Mergesort for large arrays.
- The difference in runtime becomes more pronounced as the size of the array increases, with Mergesort and Quicksort often outperforming Heapsort in terms of speed

'''


import numpy as np
import time

# Function to time the sorting algorithm
def time_sorting(array, kind='quicksort'):
    start_time = time.time()
    np.sort(array, kind=kind)
    end_time = time.time()
    return end_time - start_time

array_sizes = [1000, 10000, 100000]  # Example sizes
results = {'quicksort': [], 'mergesort': [], 'heapsort': []}

for size in array_sizes:
    data = np.random.randint(0, 101, size=size)
    for sort_type in results.keys():
        # Make a copy of the original array to ensure it's unsorted each time
        data_copy = np.copy(data)
        duration = time_sorting(data_copy, kind=sort_type)
        results[sort_type].append(duration)
        print(f"Sorting {size} elements with {sort_type}: {duration} seconds")

# Print out results or observations
for sort_type, times in results.items():
    print(f"{sort_type} times: {times}")

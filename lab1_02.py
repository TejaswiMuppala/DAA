import time
import random
import matplotlib.pyplot as plt

# Linear search function
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Binary search function
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Function to measure execution time
def measure_time(search_func, arr, key):
    start_time = time.time()
    search_func(arr, key)
    return (time.time() - start_time) * 1000  # Convert seconds to milliseconds

# Generate random array of 10000 elements
arr = [random.randint(1, 1000) for _ in range(10000)]

# Take 5 different search keys from the user
search_keys = [int(input("Enter search key {} (between 1 and 1000): ".format(i+1))) for i in range(5)]

# Measure time for linear and binary search for each key
linear_times = [measure_time(linear_search, arr, key) for key in search_keys]
binary_times = [measure_time(binary_search, sorted(arr), key) for key in search_keys]

# Plotting
plt.plot(search_keys, linear_times, label='Linear Search')
plt.plot(search_keys, binary_times, label='Binary Search')
plt.xlabel('Search Key')
plt.ylabel('Time (milliseconds)')
plt.title('Time taken by Linear and Binary Searches')
plt.legend()
plt.show()

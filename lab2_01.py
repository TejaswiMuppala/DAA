import time
import random
import matplotlib.pyplot as plt

# Selection sort algorithm
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion sort algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge sort algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Generate 1000 random integers between 1 and 10000
random_numbers = [random.randint(1, 10000) for _ in range(1000)]

# Measure time taken by each sorting algorithm
start_time = time.time()
selection_sort(random_numbers.copy())
selection_time = time.time() - start_time

start_time = time.time()
insertion_sort(random_numbers.copy())
insertion_time = time.time() - start_time

start_time = time.time()
merge_sort(random_numbers.copy())
merge_time = time.time() - start_time

# Plotting
labels = ['Selection Sort', 'Insertion Sort', 'Merge Sort']
times = [selection_time, insertion_time, merge_time]

plt.bar(labels, times, color=['red', 'green', 'blue'])
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time (seconds)')
plt.title('Time taken by Sorting Algorithms')
plt.show()

import heapq

def find_k_largest_elements(arr, k):
    min_heap = []
    # Push the first K elements into the min heap
    for i in range(k):
        heapq.heappush(min_heap, arr[i])
    
    # For the remaining elements, if an element is larger than the smallest element in the heap,
    # replace the smallest element with the current element
    for i in range(k, len(arr)):
        if arr[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, arr[i])
    
    # The min heap now contains the K largest elements
    return min_heap

# Take user input for the array
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Take user input for the value of K
K = int(input("Enter the value of K (number of largest elements to find): "))

# Find the K largest elements in the array
k_largest_elements = find_k_largest_elements(arr, K)

print("K largest elements:", k_largest_elements)

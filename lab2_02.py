import heapq

def print_sorted_lists(lists):
    min_heap = []
    # Initialize the heap with the first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i))
    
    while min_heap:
        val, index = heapq.heappop(min_heap)
        print(val, end=" ")
        # If there are more elements in the list, push the next one to the heap
        if len(lists[index]) > 1:
            heapq.heappush(min_heap, (lists[index][1], index))
            # Update the list to exclude the printed element
            lists[index] = lists[index][1:]

# Example lists
lists = [
    [10, 20, 30, 40],
    [15, 25, 35],
    [27, 29, 37, 48, 93],
    [32, 33]
]

print("Sorted Order:", end=" ")
print_sorted_lists(lists)

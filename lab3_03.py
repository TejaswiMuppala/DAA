def find_swapped_elements(arr):
    first = None
    second = None

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if first is None:
                first = i
            second = i + 1

    return first, second

def sort_array_linear_time(arr):
    first, second = find_swapped_elements(arr)

    if first is not None and second is not None:
        arr[first], arr[second] = arr[second], arr[first]

# Take user input for the array
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Sort the array in linear time
sort_array_linear_time(arr)

print("Sorted array after swapping two elements:", arr)

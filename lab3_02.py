def max_product_pair(arr):
    if len(arr) < 2:
        return None

    max_positive1 = max(arr[0], arr[1])
    max_positive2 = min(arr[0], arr[1])
    min_negative1 = min(arr[0], arr[1])
    min_negative2 = max(arr[0], arr[1])

    for num in arr[2:]:
        if num >= max_positive1:
            max_positive2 = max_positive1
            max_positive1 = num
        elif num > max_positive2:
            max_positive2 = num
        
        if num <= min_negative1:
            min_negative2 = min_negative1
            min_negative1 = num
        elif num < min_negative2:
            min_negative2 = num

    if max_positive1 * max_positive2 > min_negative1 * min_negative2:
        return max_positive1, max_positive2
    else:
        return min_negative1, min_negative2

# Take user input for the unsorted integer array
arr = list(map(int, input("Enter the unsorted integer array separated by space: ").split()))

# Find a pair with maximum product
pair = max_product_pair(arr)
if pair:
    print("Pair with maximum product:", pair)
    print("Maximum product:", pair[0] * pair[1])
else:
    print("No pair found")

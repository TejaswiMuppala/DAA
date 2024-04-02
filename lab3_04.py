def segregate_zeros_ones(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 1 and left < right:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

# Take user input for the binary array
arr = list(map(int, input("Enter the binary array elements separated by space (0's and 1's only): ").split()))

# Segregate 0's and 1's
segregate_zeros_ones(arr)

print("Array after segregating 0's and 1's:", arr)

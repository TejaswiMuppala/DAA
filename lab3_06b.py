def two_sum_sorted(arr, K):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == K:
            return True, (arr[left], arr[right])
        elif arr[left] + arr[right] < K:
            left += 1
        else:
            right -= 1
    return False, None

# Example usage
arr = [8, 4, 1, 6]
K = 10
found, pair = two_sum_sorted(arr, K)
if found:
    print("Pair with sum", K, "found:", pair)  # Output: Pair with sum 10 found: (4, 6)
else:
    print("No pair found with sum", K)

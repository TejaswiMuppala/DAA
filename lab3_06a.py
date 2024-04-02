def two_sum_brute_force(arr, K):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == K:
                return True, (arr[i], arr[j])
    return False, None

# Example usage
arr = [8, 4, 1, 6]
K = 10
found, pair = two_sum_brute_force(arr, K)
if found:
    print("Pair with sum", K, "found:", pair)  # Output: Pair with sum 10 found: (4, 6)
else:
    print("No pair found with sum", K)

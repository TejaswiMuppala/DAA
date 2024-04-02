def merge(arr, left, mid, right):
    count = 0
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            j += 1
            count += (mid - left + 1) - i
        k += 1

    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1

    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1

    return count

def merge_sort(arr, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += merge_sort(arr, left, mid)
        count += merge_sort(arr, mid + 1, right)
        count += merge(arr, left, mid, right)
    return count

# Given input
A = [10, 1, 2, 4, 13, 9, 5]

# Calculate inversion count
inversions = merge_sort(A, 0, len(A) - 1)

print("Total count of inversions:", inversions)

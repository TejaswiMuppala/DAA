def find_pairs_with_sum(arr, target_sum):
    num_set = set()
    pairs = []

    for num in arr:
        complement = target_sum - num
        if complement in num_set:
            pairs.append((num, complement))
        num_set.add(num)

    return pairs

# Take user input for the unsorted integer array
arr = list(map(int, input("Enter the unsorted integer array separated by space: ").split()))

# Take user input for the target sum
target_sum = int(input("Enter the target sum: "))

# Find pairs with the given sum
pairs = find_pairs_with_sum(arr, target_sum)
if pairs:
    print("Pairs with sum {} found:".format(target_sum), end=" ")
    for i, pair in enumerate(pairs):
        if i > 0:
            print("or", end=" ")
        print(pair, end=" ")
    print()
else:
    print("No pairs found with sum", target_sum)

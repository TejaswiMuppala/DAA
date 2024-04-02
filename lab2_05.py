def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]
    for interval in intervals[1:]:
        # Check if the current interval overlaps with the last merged interval
        if interval[0] <= merged_intervals[-1][1]:
            # Merge the intervals
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
        else:
            # No overlap, add the interval to the merged_intervals list
            merged_intervals.append(interval)

    return merged_intervals

# Example intervals: list of tuples (start_time, end_time)
intervals = [(1, 4), (2, 5), (7, 8), (6, 9)]
merged_intervals = merge_intervals(intervals)

print("Non-overlapping intervals after merging:")
for interval in merged_intervals:
    print(interval)

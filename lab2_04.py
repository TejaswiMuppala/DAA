def max_activities(activities):
    # Sort activities based on finishing time
    activities.sort(key=lambda x: x[1])
    
    # The first activity will always be selected
    selected_activities = [activities[0]]
    
    # Iterate through the remaining activities
    for activity in activities[1:]:
        # If the start time of the current activity is after or equal to the finish time
        # of the previously selected activity, then select the current activity
        if activity[0] >= selected_activities[-1][1]:
            selected_activities.append(activity)
    
    return selected_activities

# Example activities: (start_time, finish_time)
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

# Find the maximum number of activities performed by a single person
selected_activities = max_activities(activities)
max_activities_count = len(selected_activities)

print("Maximum number of activities performed by a single person:", max_activities_count)
print("Selected activities:", selected_activities)

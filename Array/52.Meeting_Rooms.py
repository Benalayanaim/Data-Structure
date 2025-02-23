#Problem https://neetcode.io/solutions/meeting-rooms
#https://leetcode.ca/2016-08-08-252-Meeting-Rooms/



"Brute force"
#Solution 1:

def can_schedule_all_meetings(intervals):
    n = len(intervals)
    for i in range(n):
        for j in range(i + 1, n):
            start1, end1 = intervals[i]
            start2, end2 = intervals[j]
            # Check for overlap
            if start1 < end2 and start2 < end1:
                return False
    return True

# Test cases
print(can_schedule_all_meetings([[0, 30], [5, 10], [15, 20]])) 
print(can_schedule_all_meetings([(5, 8), (9, 15)]))            


print("=================================================")

"optmizing by sort"
#Solution 2:
def can_schedule_all_meetings1(intervals):
    # Step 1: Sort intervals by their start times
    intervals.sort(key=lambda x: x[0])  # Sorting by start time

    # Step 2: Check for overlaps
    for i in range(len(intervals) - 1):
        # Current interval: intervals[i], Next interval: intervals[i + 1]
        if intervals[i][1] > intervals[i + 1][0]:  # Overlap condition
            return False

    # Step 3: No overlaps found
    return True

# Test cases
print(can_schedule_all_meetings1([[0, 30], [5, 10], [15, 20]])) 
print(can_schedule_all_meetings1([(5, 8), (9, 15)]))             



#Explanation : https://chatgpt.com/c/67850569-5914-800f-948b-bd92071f1f9c







print("===========================================================================")
"Built-in Method with Python"

from itertools import pairwise

def canAttendMeetings(intervals):
    intervals.sort()
    return all(a[1] <= b[0] for a, b in pairwise(intervals))

# Test cases
print(canAttendMeetings([[0, 30], [5, 10], [15, 20]])) 
print(canAttendMeetings([(5, 8), (9, 15)]))             

#####################################

from itertools import pairwise

def canAttendMeetings1(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
    return not any(a[1] > b[0] for a, b in pairwise(intervals))  # Check for conflicts

# Test cases
print(canAttendMeetings1([[0, 30], [5, 10], [15, 20]]))  # Output: False
print(canAttendMeetings1([(5, 8), (9, 15)]))              # Output: True


"Explanation "
#https://chatgpt.com/c/67850c70-ca6c-800f-ab86-e40c92690486
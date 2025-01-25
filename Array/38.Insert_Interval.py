# Problem : https://leetcode.com/problems/insert-interval/description/
"First see the editorial to understand the problem "





#Solution 1:
def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)
    
    # Step 1: Add all intervals that end before the new interval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Step 2: Merge overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # Step 3: Add all intervals that start after the new interval ends
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# Example usage
intervals1 = [[1, 3], [6, 9]]
newInterval1 = [2, 5]
print(insert(intervals1, newInterval1))  

intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval2 = [4, 8]
print(insert(intervals2, newInterval2))  



print("===============================================")
#Solution 2:
def insert(intervals, newInterval): 
        intervals.append(newInterval)
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res


# Example usage
intervals1 = [[1, 3], [6, 9]]
newInterval1 = [2, 5]
print(insert(intervals1, newInterval1))  

intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval2 = [4, 8]
print(insert(intervals2, newInterval2))  




print("===============================================")
#Solution 3:
def insert(intervals, newInterval): 
        res = []
        
        for i, (x, y) in enumerate(intervals):
            if y < newInterval[0]:
                res.append([x,y])
            elif x > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)
        res.append(newInterval)
        return res

# Example usage
intervals1 = [[1, 3], [6, 9]]
newInterval1 = [2, 5]
print(insert(intervals1, newInterval1))  

intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval2 = [4, 8]
print(insert(intervals2, newInterval2))  


print("===============================================")
#Solution 4:
def insert(intervals, newInterval):
    # If the intervals list is empty, return newInterval
    if not intervals:
        return [newInterval]

    n = len(intervals)
    target = newInterval[0]
    left, right = 0, n - 1

    # Binary search to find insertion position
    while left <= right:
        mid = (left + right) // 2
        if intervals[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Insert newInterval at the calculated position
    intervals.insert(left, newInterval)

    # Merge overlapping intervals
    res = []
    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])

    return res



# Example usage
intervals1 = [[1, 3], [6, 9]]
newInterval1 = [2, 5]
print(insert(intervals1, newInterval1))  

intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval2 = [4, 8]
print(insert(intervals2, newInterval2)) 
#Explanation : https://chatgpt.com/c/677a7ae2-23a8-800f-92b8-4135b718fca4
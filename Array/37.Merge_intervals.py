#Leetcode : https://leetcode.com/problems/merge-intervals/

"For understand how this problem work see first the Edittorial "



#Solution 1:
def merge_intervals_brute_force(intervals):
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    i = 0
    while i < len(intervals) - 1:
        # Check if intervals[i] overlaps with intervals[i+1]
        if intervals[i][1] >= intervals[i + 1][0]:
            # Merge intervals
            merged_interval = [min(intervals[i][0], intervals[i + 1][0]),
                               max(intervals[i][1], intervals[i + 1][1])]
            # Remove the two intervals and insert the merged one
            intervals.pop(i + 1)
            intervals[i] = merged_interval
        else:
            i += 1

    return intervals

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals_brute_force(intervals))

print("================================")

#Solution 2:

def merge(intervals): 
        intervals = sorted(intervals,key = lambda x: x[0])
        merged_intervals = []

        for interval in intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)

            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals_brute_force(intervals))


print("================================")


#Solution 3:
def merge(intervals): 
        if not intervals:
            return []

        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last_added_interval = result[-1]

            # If the current interval overlaps with the last added interval, 
            # merge them
            if last_added_interval[1] >= intervals[i][0]:
                last_added_interval[1] = max(last_added_interval[1], intervals[i][1])
            else:
                # Otherwise, add the current interval to the result
                result.append(intervals[i])

        return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals_brute_force(intervals))



"Fy ChatGpt mtec3iii"
"Fy ekher haja gothelle bech yfessrhelii ekhtarr 3/4 lokhriin 1/4 w2/4 w 4/4 meghiir metdhay3 waqtek fiihom"

#Explanation : https://chatgpt.com/c/677995fb-f6c4-800f-98a0-95d4a7e645ee

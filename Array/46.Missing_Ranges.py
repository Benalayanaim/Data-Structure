"Problem"
#https://www.youtube.com/watch?v=EKJQJBFCoE4&t=1s
#https://leetcode.ca/2016-05-11-163-Missing-Ranges/



#Solution 1:
def findMissingRanges(nums, lower, upper):
    def formatRange(start, end):
        # Helper function to format the range
       # Single number case
        if start == end:
            return str(start)
        # Range case
        return f"{start}->{end}"
    
    # Initialize result list
    result = []
    
    # Start the current pointer at lower
    prev = lower - 1  # Tracks the end of the last included range

    # Iterate through the array, plus one additional step for `upper + 1`
    for curr in nums + [upper + 1]:
        if curr - prev > 1:  # If there is a gap
            result.append(formatRange(prev + 1, curr - 1))
        prev = curr  # Move the `prev` pointer
    
    return result

# Example 1
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper)) 

# Example 2
nums = []
lower = 1
upper = 1
print(findMissingRanges(nums, lower, upper)) 

# Example 3
nums = []
lower = -3
upper = 1
print(findMissingRanges(nums, lower, upper))  





print("========================================")

#Solution 2:
def findMissingRanges2(nums, lower, upper):
    sol = []
    left = lower

    for each_nums in nums:

        if left <= each_nums - 1:
            sol.append(f"{left}-> {each_nums-1}")
            left = each_nums + 1
        else:
            left = each_nums + 1

    if left <= upper:
        sol.append(f"{left}->{upper}")

    return sol

# Example 1
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges2(nums, lower, upper)) 

# Example 2
nums = []
lower = 1
upper = 1
print(findMissingRanges2(nums, lower, upper)) 

# Example 3
nums = []
lower = -3
upper = 1
print(findMissingRanges2(nums, lower, upper))  





print("========================================")

#Solution 3:
from itertools import pairwise
def findMissingRanges3(nums, lower, upper):
        n = len(nums)
        if n == 0:
            return [[lower, upper]]
        ans = []
        if nums[0] > lower:
            ans.append([lower, nums[0] - 1])
        for a, b in pairwise(nums):
            if b - a > 1:
                ans.append([a + 1, b - 1])
        if nums[-1] < upper:
            ans.append([nums[-1] + 1, upper])
        return ans

# Example 1
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges3(nums, lower, upper)) 

# Example 2
nums = []
lower = 1
upper = 1
print(findMissingRanges3(nums, lower, upper)) 

# Example 3
nums = []
lower = -3
upper = 1
print(findMissingRanges3(nums, lower, upper))  





print("========================================")

#Solution 4:
def findMissingRanges4(nums, lower, upper):
    def getRange(lo: int, hi: int) -> list[int]:
      if lo == hi:
        return [lo, lo]
      return [lo, hi]

    if not nums:
      return [getRange(lower, upper)]

    ans = []

    if nums[0] > lower:
      ans.append(getRange(lower, nums[0] - 1))

    for prev, curr in zip(nums, nums[1:]):
      if curr > prev + 1:
        ans.append(getRange(prev + 1, curr - 1))

    if nums[-1] < upper:
      ans.append(getRange(nums[-1] + 1, upper))

    return ans

# Example 1
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges4(nums, lower, upper)) 

# Example 2
nums = []
lower = 1
upper = 1
print(findMissingRanges4(nums, lower, upper)) 

# Example 3
nums = []
lower = -3
upper = 1
print(findMissingRanges4(nums, lower, upper))  



"Fy chat mteiiii"
#Explanation 
#https://chatgpt.com/c/678251c8-78f4-800f-9421-40027a411125
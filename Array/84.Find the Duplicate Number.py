#Problem
#https://leetcode.com/problems/find-the-duplicate-number/description/?envType=problem-list-v2&envId=array



"Hash set"
#Solution 1:

def findDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None

nums = [1,2,2,3,4] 
print(findDuplicate(nums))

nums = [4,2,3,3,8]
print(findDuplicate(nums))



print("======================================")
"Sort Approach"

#Solution 2:
def findDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]
    return None
nums = [1,2,2,3,4] 
print(findDuplicate(nums))

nums = [4,2,3,3,8]
print(findDuplicate(nums))




print("======================================")

#Solution 2:
def findDuplicate(nums):
    nums.sort()
    i=0
    while i<(len(nums)-1):
        if nums[i]==nums[i+1]:
            return nums[i]
        i=i+1

    return None

nums = [1,2,2,3,4] 
print(findDuplicate(nums))

nums = [4,2,3,3,8]
print(findDuplicate(nums))





print("======================================")
"Counter Approach"

#Solution 2:
from collections import Counter
def findDuplicate(nums):
        count_nums = Counter(nums)

        for i in count_nums:
            if count_nums[i] > 1:
                return i
        return None

nums = [1,2,2,3,4] 
print(findDuplicate(nums))

nums = [4,2,3,3,8]
print(findDuplicate(nums))






print("======================================")
"Brute Force"

#Solution 2:
def findDuplicate(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i+1,n):
            # Check if the current number is equal to any of the following numbers
            if nums[i] == nums[j]:
                # If a duplicate is found, return the duplicate number
                return nums[i]
    # If no duplicate is found after checking the entire list, return None
    return None

nums = [1,2,2,3,4] 
print(findDuplicate(nums))

nums = [4,2,3,3,8]
print(findDuplicate(nums))

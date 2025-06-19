"Problem"
#https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array




"Linear Search"

#Solution 1:
def searchInsert(nums, target):
        if not nums:
            return 0
        
        for i, num in enumerate(nums):
            if num >= target:
                return i
        
        return len(nums)

#Expamle Usage
nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))


"Binary Search"


print("=======================================================")
#Solution 1:
def searchInsert(nums, target):
        left = 0              # is initialized to the start of the array (index 0).
        right = len(nums) - 1 # is initialized to the end of the array (index len(nums) - 1 because we start from o indexed this  why we do -1).

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left


#Expamle Usage
nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))



#Explanation : https://chat.deepseek.com/a/chat/s/009cd630-adb0-4d19-86d5-f5ae74bbab51


print("=======================================================")

import bisect
#Solution 1:
def searchInsert(nums, target):
    return bisect.bisect_left(nums, target)

#Expamle Usage
nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))
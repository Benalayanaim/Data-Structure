#Problem
#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/


#Solution N1:
def search(nums, target):
    
    for i in range(len(nums)):
        if nums[i] == target:
            
            return True
    
    return False

nums = [2,5,6,0,0,1,2]
target = 0
print(search(nums, target))

print("=====================")

#Solution 2

class Solution:
    def search(nums, target: int) -> bool:
        # Initilize two pointers
        begin = 0
        end = len(nums) - 1 
        while begin <= end:
            mid = (begin + end)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[end]: # Fail to estimate which side is sorted
                end -= 1  # In worst case: O(n)
            elif nums[mid] > nums[end]: # Left side of mid is sorted
                if  nums[begin] <= target and target < nums[mid]: # Target in the left side
                    end = mid - 1
                else: # in right side
                    begin = mid + 1
            else: # Right side is sorted
                if  nums[mid] < target and target <= nums[end]: # Target in the right side
                    begin = mid + 1
                else: # in left side
                    end = mid - 1
        return False

nums = [2,5,6,0,0,1,2]
target = 0
print(search(nums, target))

print("=====================")

#Solution 3

def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return True
        
        # Handle duplicates
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        # Left side is sorted
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right side is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return False
nums = [2,5,6,0,0,1,2]
target = 0
print(search(nums, target))





"Explanation : "

#https://chatgpt.com/c/6756b161-9e74-8007-9bea-e485158047c1
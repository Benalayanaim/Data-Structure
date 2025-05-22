#https://leetcode.ca/2019-01-23-1150-Check-If-a-Number-Is-Majority-Element-in-a-Sorted-Array/





#Solution 1:

def isMajorityElement(nums, target):
    def find_first_occurrence(nums, target):
        left, right = 0, len(nums) - 1
        first_occurrence = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            if nums[mid] == target:
                first_occurrence = mid
        return first_occurrence

    def find_last_occurrence(nums, target):
        left, right = 0, len(nums) - 1
        last_occurrence = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] == target:
                last_occurrence = mid
        return last_occurrence

    first = find_first_occurrence(nums, target)
    if first == -1:
        return False

    last = find_last_occurrence(nums, target)
    count = last - first + 1

    return count > len(nums) / 2

# Example usage:
nums1 = [2, 4, 5, 5, 5, 5, 5, 6, 6]
target1 = 5
print(isMajorityElement(nums1, target1))

nums2 = [10, 100, 101, 101]
target2 = 101
print(isMajorityElement(nums2, target2))  




print("==========================================================")


#Solution 2:
def is_majority_element(nums, target):

    # Find the first occurrence of the target in the sorted array
    first_occurrence = None
    for i, num in enumerate(nums):
        if num == target:
            first_occurrence = i
            break

    # If the target is not found, return False
    if first_occurrence is None:
        return False

    # Find the last occurrence of the target in the sorted array
    last_occurrence = None
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            last_occurrence = i
            break

    # Calculate the count of the target in the array
    count = last_occurrence - first_occurrence + 1

    # Check if the target is a majority element
    return count > len(nums) / 2


# Example usage:
nums = [2, 4, 5, 5, 5, 5, 5, 6, 6]
target = 5
result = is_majority_element(nums, target)
print(result)  

nums = [10, 100, 101, 101]
target = 101
result = is_majority_element(nums, target)
print(result)  


print("==========================================================")


#Solution 3:
from bisect import bisect_left, bisect_right

def isMajorityElement(nums, target):
    # Find the leftmost and rightmost indices of the target using binary search
    left_index = bisect_left(nums, target)
    right_index = bisect_right(nums, target)
    
    # Calculate the count of the target in the array
    count = right_index - left_index
    
    # Check if the target count is more than half the length of the array
    return count > len(nums) // 2

# Example 1
nums1 = [2, 4, 5, 5, 5, 5, 5, 6, 6]
target1 = 5
print(isMajorityElement(nums1, target1))  

# Example 2
nums2 = [10, 100, 101, 101]
target2 = 101
print(isMajorityElement(nums2, target2))  



#Explanation : https://chatgpt.com/c/6794c7c7-1a58-800f-8653-9cb953f7d0db

"Resource to understand bisect_left vs bisect_right and why not do in the count +1 like the other solution"
#https://medium.com/@yohoso/difference-between-bisect-left-and-bisect-right-in-python-32df4eb2cc06

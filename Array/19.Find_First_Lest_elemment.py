#Find First and Last of Element in Sorted Array
#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/





#Solution 1:

def search_range(nums, target):
    # Initialize start and end indices
    start = -1
    end = -1

    # Iterate through the array
    for i in range(len(nums)):
        if nums[i] == target:
            # If start is not set, set it to the current index
            if start == -1:
                start = i
            # Update the end index to the current index
            end = i

    return [start, end]

# Example usage:
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(search_range(nums1, target1))  

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(search_range(nums2, target2))  

nums2 = [5, 7, 7, 8, 8, 10, 4]
target2 = 4
print(search_range(nums2, target2))  

nums3 = []
target3 = 0
print(search_range(nums3, target3))  


print("=================================")

#Solution 2 :
def searchRange (nums, target):
    def search(x):
        lo = 0
        hi = len(nums)

        while lo< hi :
            mid = (lo + hi) // 2

            if nums[mid] < x:

                lo = mid +1
            else :
             
                hi = mid                    
        return lo
    
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]


# Example usage:
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(search_range(nums1, target1))  

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(search_range(nums2, target2))  

nums2 = [5, 7, 7, 8, 8, 10, 4]
target2 = 4
print(search_range(nums2, target2))  

nums3 = []
target3 = 0
print(search_range(nums3, target3))  




print("=================================")

#Solution 3 :

def searchRange(nums , target):
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last
        
        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]

# Example usage:
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(search_range(nums1, target1))  

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(search_range(nums2, target2))  

nums2 = [5, 7, 7, 8, 8, 10, 4]
target2 = 4
print(search_range(nums2, target2))  

nums3 = []
target3 = 0
print(search_range(nums3, target3))  

"""Explanation binary Search
Initialize two variables, first and last, to -1.
Perform a binary search to find the target element.
When you find the target element, update first to the current index and continue searching for the first occurrence in the left subarray.
Similarly, update last to the current index and continue searching for the last occurrence in the right subarray.
Continue until the binary search terminates.
Return first and last."""

print("=================================")

#Solution 4 :

def searchRange(nums, target):
        left, right = 0, len(nums) - 1
        first, last = -1, -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first = mid
                last = mid
                while first > 0 and nums[first - 1] == target:
                    first -= 1
                while last < len(nums) - 1 and nums[last + 1] == target:
                    last += 1
                return [first, last]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [first, last]
# Example usage:
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(search_range(nums1, target1))  

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(search_range(nums2, target2))  

nums2 = [5, 7, 7, 8, 8, 10, 4]
target2 = 4
print(search_range(nums2, target2))  

nums3 = []
target3 = 0
print(search_range(nums3, target3))  


"""Explanation : Two-Pointer Approach:
Initialize two pointers, left and right, to the beginning and end of the array, respectively.
Initialize two variables, first and last, to -1.
Use a while loop with the condition left <= right.
Calculate the middle index as (left + right) / 2.
If the middle element is equal to the target, update first and last accordingly and adjust the pointers.
If the middle element is less than the target, update left.
If the middle element is greater than the target, update right.
Continue the loop until left is less than or equal to right.
Return first and last."""


#"Explanation"
#https://chatgpt.com/c/67580dcd-2f5c-8007-8da3-345300fe8c32
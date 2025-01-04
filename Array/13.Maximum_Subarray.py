#https://leetcode.com/problems/maximum-subarray/description/


#SUbArray ??? : https://www.geeksforgeeks.org/array-subarray-subsequence-and-subset/



#Solution 1:
def max_subarray_sum(nums):
    # Initialize variables
    current_sum = 0
    max_sum = float('-inf')
    
    # Iterate through the array
    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        # Reset current_sum to 0 if it becomes negative
        if current_sum < 0:
            current_sum = 0
            
    return max_sum

# Test cases
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1]
nums3 = [5, 4, -1, 7, 8]

print(max_subarray_sum(nums1))  # Output: 6
print(max_subarray_sum(nums2))  # Output: 1
print(max_subarray_sum(nums3))  # Output: 23


print("====================================")

#Solution 2:


def maxSubarraySum(arr):
    res = arr[0]
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(res, maxEnding)
    
    return res
# Test cases
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1]
nums3 = [5, 4, -1, 7, 8]

print(max_subarray_sum(nums1))  # Output: 6
print(max_subarray_sum(nums2))  # Output: 1
print(max_subarray_sum(nums3))  # Output: 23


"Explantion"
#https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

print("====================================")

#Solution 2:

def maxSubArray(nums):
    res = -float('inf')  # Initialize `res` to the smallest possible value.

    for i in range(len(nums)):  # Start of the outer loop, representing the starting index of the subarray.
        curr_sum = 0  # Initialize the current subarray sum to 0.
       
        for j in range(i, len(nums)):  # Inner loop, iterating from the starting index `i` to the end of the array.
            curr_sum += nums[j]  # Add the element at index `j` to the current subarray sum.
            res = max(res, curr_sum)  # Update `res` if `curr_sum` is larger.
    
    return res  # Return the maximum sum found.


nums = [-2,1,-3,4,-1,2,1,-5,4]
nums1= [10, 3, -1, -2]
nums2= [5,4,-1,7,8] 

print(maxSubArray(nums))
print(maxSubArray(nums1))
print(maxSubArray(nums2))


#Explanation
"We can start with brute-force by trying out every possible sub-array in nums and choosing the one with maximum sum."
"""The idea is to run two nested loops to iterate over all possible subarrays and find 
the maximum sum. The outer loop will mark the starting point of a subarray and inner loop
will mark the ending point of the subarray."""





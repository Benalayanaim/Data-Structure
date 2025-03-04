"Problem :"
# https://www.youtube.com/watch?v=4FbTZeyAGrc
# https://leetcode.ca/2018-12-03-1099-Two-Sum-Less-Than-K/





#Solution 1:
def twoSumLessThanK(nums, k):
    # Sort the list to apply the two-pointer technique
        nums.sort()
      
        # Initialize two pointers, one at the start and one at the end of the list
        left_pointer, right_pointer = 0, len(nums) - 1
      
        # Initialize the answer variable with -1 which will be returned if no suitable pair is found
        max_sum = -1
      
        # Iterate until the two pointers meet
        while left_pointer < right_pointer:
            # Calculate the current sum of the values pointed by the two pointers
            current_sum = nums[left_pointer] + nums[right_pointer]
          
            # If the sum is less than k, it's a potential candidate for our answer
            if current_sum < k:
                # Update the answer with the maximum sum encountered which is less than k
                max_sum = max(max_sum, current_sum)
                # Move the left pointer to the right to potentially increase the sum
                left_pointer += 1
            else:
                # If the sum is greater than or equal to k, move the right pointer to the left
                # This is to try and find a smaller sum that is less than k
                right_pointer -= 1
      
        # Return the maximum sum that we have found which is less than k, or -1 if there is no such sum
        return max_sum


# Test cases
nums1, k1 = [34, 23, 1, 24, 75, 33, 54, 8], 60
nums2, k2 = [10, 20, 30], 15

print(twoSumLessThanK(nums1, k1))  
print(twoSumLessThanK(nums2, k2))  


print("============================================")

#Solution 2
def twoSumLessThanK(nums, k):
    size = len(nums)
    sum_less_k = 0  # Keep track of the maximum sum less than k

    for i in range(size):
        for j in range(i + 1, size):
            if nums[i] + nums[j] > sum_less_k and nums[i] + nums[j] < k:
                sum_less_k = nums[i] + nums[j]
    
    if sum_less_k == 0:  # If no valid pair is found
        return -1
    return sum_less_k

# Test cases
nums1, k1 = [34, 23, 1, 24, 75, 33, 54, 8], 60
nums2, k2 = [10, 20, 30], 15

print(twoSumLessThanK(nums1, k1))  
print(twoSumLessThanK(nums2, k2)) 






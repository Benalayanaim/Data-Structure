#Problem : https://leetcode.com/problems/find-pivot-index/?envType=problem-list-v2&envId=array




#Solution 1:
def pivotIndex(nums):
    total_sum = sum(nums)  # Compute total sum of the array
    left_sum = 0           # Initialize left sum as 0
    
    for i, num in enumerate(nums):
        # Check if left_sum equals the right sum
        if left_sum == (total_sum - left_sum - num):
            return i
        left_sum += num  # Update left_sum by adding the current number
    
    return -1  # Return -1 if no pivot index is found

# Examples
print(pivotIndex([1, 7, 3, 6, 5, 6]))  
print(pivotIndex([1, 2, 3]))           
print(pivotIndex([2, 1, -1]))          



print("==============================================")
#Solution 2:
def pivotIndex(nums):
        total = sum(nums)
        left_total = 0

        for i in range(len(nums)):
            right_total = total - left_total - nums[i]

            if right_total == left_total:
                return i
            
            left_total += nums[i]
        
        return -1

# Examples
print(pivotIndex([1, 7, 3, 6, 5, 6]))  
print(pivotIndex([1, 2, 3]))           
print(pivotIndex([2, 1, -1]))          




print("==============================================")
#Solution 3:
def pivotIndex(nums):
    left, right = 0, sum(nums)
    for idx, val in enumerate(nums):
        right -= val
        if left == right:
            return idx
        left += val
    return -1

# Examples
print(pivotIndex([1, 7, 3, 6, 5, 6]))  
print(pivotIndex([1, 2, 3]))           
print(pivotIndex([2, 1, -1]))          






print("==============================================")
#Solution 4:
def pivotIndex(nums): 
    for i in range(len(nums)):
        left_sum = sum(nums[:i])       # Sum of elements to the left of index i
        right_sum = sum(nums[i+1:])   # Sum of elements to the right of index i
        if left_sum == right_sum:     # Check if left sum equals right sum
            return i
    return -1


# Examples
print(pivotIndex([1, 7, 3, 6, 5, 6]))  
print(pivotIndex([1, 2, 3]))           
print(pivotIndex([2, 1, -1]))          



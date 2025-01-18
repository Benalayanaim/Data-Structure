"Problem"
#https://leetcode.com/problems/subsets-ii/description/




#Solution N1:

def subsetsWithDup(nums):
    # Step 1: Sort the array to group duplicates together
    nums.sort()
    
    # Step 2: Initialize the result with the empty subset
    result = [[]]
    
    # Step 3: Iterate through the elements of nums
    prev_size = 0  # Tracks the size of the result from the previous iteration
    for i in range(len(nums)):
        # Determine where to start adding new subsets
        start_idx = prev_size if i > 0 and nums[i] == nums[i - 1] else 0
        prev_size = len(result)  # Update the size of the result
        
        # Add the current number to existing subsets
        for j in range(start_idx, len(result)):
            new_subset = result[j] + [nums[i]]
            result.append(new_subset)
    
    return result

# Example 1
nums1 = [1, 2, 2]
print("Input:", nums1)
print("Output:", subsetsWithDup(nums1))

# Example 2
nums2 = [0]
print("Input:", nums2)
print("Output:", subsetsWithDup(nums2))



print("========================================")

#Solution N2:

def subsetsWithDup1(nums):
    # Step 1: Sort the array to group duplicates together
    nums.sort()
    
    # Step 2: Initialize the result list
    result = []
    
    # Step 3: Define a recursive function to generate subsets
    def backtrack(start, current_subset):
        # Add the current subset to the result
        result.append(list(current_subset))
        
        # Step 4: Iterate through the elements starting from 'start'
        for i in range(start, len(nums)):
            # Skip duplicates (if current number is the same as the previous and i > start)
            if i > start and nums[i] == nums[i - 1]:
                continue
            
            # Include nums[i] in the current subset
            current_subset.append(nums[i])
            
            # Recurse to add the next elements
            backtrack(i + 1, current_subset)
            
            # Backtrack: Remove the last element to try the next possibility
            current_subset.pop()
    
    # Step 5: Start the backtracking process
    backtrack(0, [])
    
    # Return the result containing all unique subsets
    return result

# Example 1
nums1 = [1, 2, 2]
print("Input:", nums1)
print("Output:", subsetsWithDup1(nums1))

# Example 2
nums2 = [0]
print("Input:", nums2)
print("Output:", subsetsWithDup1(nums2))



print("========================================")

#Solution N2:
def subsetsWithDup2(nums):
    res = []  # Initialize the result list to store all unique subsets
    nums.sort()  # Sort the input array to group duplicates together
    dfs(nums, 0, [], res)  # Start the DFS with an empty path
    return res  # Return the result list
    
def dfs(nums, index, path, res):
    res.append(path)  # Add the current subset (path) to the result
    for i in range(index, len(nums)):  # Loop through the elements starting at `index`
        if i > index and nums[i] == nums[i-1]:  # Skip duplicates
            continue
        dfs(nums, i+1, path+[nums[i]], res)  # Recursive call with the updated path


# Example 1
nums1 = [1, 2, 2]
print("Input:", nums1)
print("Output:", subsetsWithDup2(nums1))

# Example 2
nums2 = [0]
print("Input:", nums2)
print("Output:", subsetsWithDup2(nums2))






"Explanation"
#https://chatgpt.com/c/67691c81-41e0-8007-8106-214826b20193


"the differece between Subset and subset_II"
#https://chatgpt.com/c/676930ea-2cc4-8007-adeb-25b36daf458c
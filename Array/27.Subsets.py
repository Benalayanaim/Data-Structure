"Problem"
#https://leetcode.com/problems/subsets/description/





#Solution 1:

def subsets1(nums):
    result = [[]]
    for num in nums:
        result += [curr + [num] for curr in result]
    return result

nums = [1,2,3]
print(subsets1(nums))

nums2 = []
print(subsets1(nums2))

"""Explanation :
Step-by-Step Walkthrough:
1/Initially, the result list contains only the empty subset, [].
2/We iterate over each element in nums.

3/For the first element 1:
We clone the existing subsets in result, which is currently [].
We add 1 to each cloned subset and add them back to result. So, result = [[], [1]].

4/For the second element 2:
We clone the existing subsets in result, which are [[], [1]].
We add 2 to each cloned subset and add them back to result. So, result = [[], [1], [2], [1, 2]].

5/For the third element 3:
We clone the existing subsets in result, which are [[], [1], [2], [1, 2]].
We add 3 to each cloned subset and add them back to result. So, result = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].

6/After iterating through all elements in nums, the result contains all subsets of [1, 2, 3], including the empty subset."""


print("=================================")


#Solution 2:
"""
--Use bit manipulation to generate all possible combinations.
--For a set with n elements, there are 2^n possible subsets.
--Iterate from 0 to 2^n - 1 and for each integer, consider the set bits as indices of elements to include in the subset.
--This approach is efficient in terms of time complexity, as it avoids recursion and extra space.
"""

def subsets2(nums):
    n = len(nums)
    power_set = []
    
    # There are 2^n subsets for a set of size n
    total_subsets = 1 << n  # This is equivalent to 2^n
    
    # Iterate through all numbers from 0 to 2^n - 1
    for i in range(total_subsets):
        subset = []
        for j in range(n):
            # Check if the jth bit in i is set
            if i & (1 << j):
                subset.append(nums[j])
        power_set.append(subset)
    
    return power_set

# Example usage:
nums1 = [1, 2, 3]
print(subsets2(nums1))  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

nums2 = [0]
print(subsets2(nums2))  # Output: [[], [0]]

"""Explanation
Step-by-Step Walkthrough:

1/Initially, the result list is empty.

2/We iterate over all possible subsets using bit manipulation. Since there are 3 elements in nums, there will be 2^3 = 8 subsets.

3/We start the iteration from i = 0 to i = 7, inclusive.

4/For each value of i, we check the binary representation of i to determine which elements to include in the subset.

5/For i = 0, binary representation is 000. It means the empty subset, so we add [] to the result.

6/For i = 1, binary representation is 001. It means including only the third element (nums[2] = 3) in the subset. So, we add [3] to the result.

7/For i = 2, binary representation is 010. It means including only the second element (nums[1] = 2) in the subset. So, we add [2] to the result.

8/For i = 3, binary representation is 011. It means including the second and third elements (nums[1] = 2 and nums[2] = 3) in the subset. So, we add [2, 3] to the result.

9/For i = 4, binary representation is 100. It means including only the first element (nums[0] = 1) in the subset. So, we add [1] to the result.

10/For i = 5, binary representation is 101. It means including the first and third elements (nums[0] = 1 and nums[2] = 3) in the subset. So, we add [1, 3] to the result.

11/For i = 6, binary representation is 110. It means including the first and second elements (nums[0] = 1 and nums[1] = 2) in the subset. So, we add [1, 2] to the result.

12/For i = 7, binary representation is 111. It means including all elements (nums[0] = 1, nums[1] = 2, and nums[2] = 3) in the subset. So, we add [1, 2, 3] to the result.

13/After iterating through all possible subsets, the result contains all subsets of [1, 2, 3], including the empty subset, which is [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]."""




print("=================================")

#Solution 3:
def subsets3(nums):
    def backtrack(start, path):
        # Append the current subset (path) to the result
        result.append(path[:])
        
        # Explore further by including each element starting from 'start'
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            path.append(nums[i])
            
            # Recurse to build further subsets
            backtrack(i + 1, path)
            
            # Backtrack: Remove nums[i] to try the next possibility
            path.pop()
    
    result = []
    backtrack(0, [])
    return result

# Example Usage
nums1 = [1, 2, 3]
print(subsets3(nums1))  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

nums2 = [0]
print(subsets3(nums2))  # Output: [[], [0]]




print("=================================")

#Solution 4:

def subsets4(nums): 
    def backtrack(start, path):
        # Add the current subset to the result
        result.append(path)
        
        # Loop through the elements starting from 'start'
        for i in range(start, len(nums)):
            # Recurse with the next index and the updated path
            backtrack(i + 1, path + [nums[i]])

    result = []
    backtrack(0, [])
    return result

# Example Usage
nums1 = [1, 2, 3]
print(subsets4(nums1))  

nums2 = [0]
print(subsets4(nums2)) 



print("===========================================")


#Solution 5:
def subsets5(nums):
    res = []  # Initialize the result list to store all subsets
    dfs(sorted(nums), 0, [], res)  # Call the DFS helper function
    return res

def dfs(nums, index, path, res):
    res.append(path)  # Add the current subset (path) to the result list
    for i in range(index, len(nums)):  # Loop through all elements from 'index'
        dfs(nums, i + 1, path + [nums[i]], res)  # Recursive call with updated path

# Example Usage
nums1 = [1, 2, 3]
print(subsets5(nums1))  

nums2 = [0]
print(subsets5(nums2)) 


#Explanation : https://chatgpt.com/c/67629d5a-6dd4-8007-8ba1-70e5074ab53c


"Another solution with Python built-in Method : https://chatgpt.com/c/6762ab08-c35c-8007-a2d6-67d3215ca9b2"


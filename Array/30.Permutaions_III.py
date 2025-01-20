"Problem"
#https://leetcode.com/problems/permutations-ii/description/





#Solution 1
def permuteUnique(nums):
    """
    Return all unique permutations of the list nums.
    """
    # Sort to group duplicate elements
    nums.sort()
    results = []
    used = [False] * len(nums)

    def backtrack(path):
        # If the current permutation is complete, add it to results
        if len(path) == len(nums):
            results.append(path[:])
            return
        
        for i in range(len(nums)):
            # If nums[i] is already used, skip
            if used[i]:
                continue
            
            # If nums[i] is the same as nums[i-1] and nums[i-1] was not used,
            # it would create a duplicate permutation. Skip it.
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            
            # Mark the element as used and explore further
            used[i] = True
            path.append(nums[i])
            
            backtrack(path)
            
            # Backtrack: unmark and remove the element
            used[i] = False
            path.pop()
    
    backtrack([])
    return results

# Example usage:
if __name__ == "__main__":
    # Example 1
    nums1 = [1, 1, 2, 1]
    print(permuteUnique(nums1))

    nums2 = [1, 2, 3]
    print(permuteUnique(nums2))
   


print("===============================================")

#Solution 2
from collections import Counter

def permuteUnique(nums):
    """
    Returns all unique permutations of nums using a frequency (Counter) approach.
    """
    res = []
    
    def dfs(counter, path):
        # Base case: if the current permutation has the same length as nums,
        # it's complete; add it to results.
        if len(path) == len(nums):
            res.append(path)
            return
        
        # Try using each distinct number available in 'counter'
        for x in counter:
            if counter[x] > 0:
                # Use this number 'x'
                counter[x] -= 1
                
                # Recurse with 'x' added to the current permutation path
                dfs(counter, path + [x])
                
                # Backtrack: restore the count
                counter[x] += 1
    
    # Build a frequency map for the elements in nums
    freq_counter = Counter(nums)
    
    # Start the DFS with an empty path
    dfs(freq_counter, [])
    
    return res

# Example 1
nums1 = [1, 1, 2, 1]
print(permuteUnique(nums1))

nums2 = [1, 2, 3]
print(permuteUnique(nums2))

print("===============================================")

#Solution 3

def permuteUnique(nums):
    ans = []

    def permute(res, nums):
        # Base case: if there are no elements left to pick, we have a complete permutation
        if len(nums) == 0:
            ans.append(res)
            return

        # Iterate through the current list of numbers
        for i in range(len(nums)):
            # Skip duplicates: if the current value is the same as the previous one,
            # we don't generate permutations starting from this value again
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Choose nums[i], and recurse on the remaining array
            permute(res + [nums[i]], nums[:i] + nums[i+1:])

    # Sort the numbers so that duplicates are adjacent
    nums.sort()
    # Begin with an empty current permutation and the full list of numbers
    permute([], nums)
    return ans


# Example 1
nums1 = [1, 1, 2, 1]
print(permuteUnique(nums1))

nums2 = [1, 2, 3]
print(permuteUnique(nums2))

print("===============================================")

#Solution 4

from typing import List
from collections import Counter

def permuteUnique(nums: List[int]):
    permutations = []
    counter = Counter(nums)  # frequency map of each distinct number

    def findAllPermutations(res):
        # If the current partial permutation 'res' has used all numbers,
        # we have a complete permutation.
        if len(res) == len(nums):
            permutations.append(res)
            return
        
        # Try using each distinct number in the counter
        for key in counter:
            if counter[key] > 0:
                # Choose this 'key' by decrementing its count
                counter[key] -= 1
                
                # Explore further by appending this key to the permutation
                findAllPermutations(res + [key])
                
                # Backtrack: restore the count after returning
                counter[key] += 1
    
    # Start the recursive process with an empty list
    findAllPermutations([])
    return permutations


# Example 1
nums1 = [1, 1, 2, 1]
print(permuteUnique(nums1))

nums2 = [1, 2, 3]
print(permuteUnique(nums2))


#Explanation : https://chatgpt.com/c/676c197e-82f0-8007-8510-376525749127





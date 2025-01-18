"Problem"
#https://leetcode.com/problems/permutations/




#Solution 1:

def permute(nums):
    """
    Given a list of distinct integers `nums`, return all possible permutations.
    """
    results = []
    
    def backtrack(start_index):
        # If we've placed every number, record the current permutation
        if start_index == len(nums):
            results.append(nums[:])  # Make a copy of the current permutation
            return
        
        for i in range(start_index, len(nums)):
            # Swap current element with the start_index element
            nums[start_index], nums[i] = nums[i], nums[start_index]
            # Recurse for the next position
            backtrack(start_index + 1)
            # Swap back to restore the original list state
            nums[start_index], nums[i] = nums[i], nums[start_index]
    
    backtrack(0)
    return results


# Example usage:
if __name__ == "__main__":
    print(permute([1, 2, 3]))
   
    
    print(permute([0, 1]))
   

    print(permute([1]))
   



print("==============================================")

#Solution 2:
def permute(nums) :
    def backtrack(nums, path):
        # Base case: if there are no more numbers to pick from,
        # we've formed a complete permutation.
        if not nums:
            result.append(path)
            return
        
        # Otherwise, try each element in nums as the next candidate.
        for i in range(len(nums)):
            # Pick nums[i] and recurse on the remaining elements
            backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
    
    result = []
    backtrack(nums, [])
    return result

print(permute([1, 2, 3]))
   
    
print(permute([0, 1]))
   

print(permute([1]))
   


print("==============================================")

#Solution 3:

def permute(nums):
    def dfs(path, used):
        # If the current path is as long as nums, we've formed a complete permutation
        if len(path) == len(nums):
            result.append(path[:])  # Append a copy of path to result
            return
        
        # Explore using each number that hasn't been used yet
        for i in range(len(nums)):
            if not used[i]:
                # Choose nums[i] and mark it as used
                path.append(nums[i])
                used[i] = True
                
                # Recurse with the updated path and used array
                dfs(path, used)
                
                # Backtrack: remove nums[i] from the path, mark it as unused
                path.pop()
                used[i] = False
    
    result = []
    used = [False] * len(nums)  # Tracks whether nums[i] is already in the current path
    
    # Start DFS with an empty path and a fresh used array
    dfs([], used)
    
    return result

print(permute([1, 2, 3]))
   
    
print(permute([0, 1]))
   

print(permute([1]))
   

print("==============================================")

#Solution 4:
def permute(nums):
    ans = []

    def backtrack(curr_lst):
        # Base Case:
        # If we've used all numbers, `curr_lst` is a complete permutation.
        if len(curr_lst) == len(nums):
            ans.append(curr_lst.copy())  # Make sure to store a *copy* instead of the reference
            return  # Important to return here
        
        # Recursive Case:
        # Try placing each number in `nums` that is *not* yet in `curr_lst`.
        for num in nums:
            if num not in curr_lst:
                curr_lst.append(num)       # Choose 'num'
                backtrack(curr_lst)        # Explore deeper
                curr_lst.pop()             # Backtrack (undo the choice)

    backtrack([])  # Start with an empty current list
    return ans



print(permute([1, 2, 3]))
   
    
print(permute([0, 1]))
   

print(permute([1]))




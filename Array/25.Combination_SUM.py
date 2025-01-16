"Problem"
#https://leetcode.com/problems/combination-sum/description/



def combinationSum(candidates, target):
    def backtrack(start, current_combination, current_sum):
        # Base case: if the sum equals the target, add the combination to the result
        if current_sum == target:
            result.append(list(current_combination))
            return
        # If the sum exceeds the target, stop exploring further
        if current_sum > target:
            return
        
        # Explore all candidates starting from the current index
        for i in range(start, len(candidates)):
            # Include the current candidate
            current_combination.append(candidates[i])
            # Recurse with the same index (unlimited use of the same number)
            backtrack(i, current_combination, current_sum + candidates[i])
            # Backtrack: remove the last number added
            current_combination.pop()
    
    result = []
    backtrack(0, [], 0)  # Start the recursion
    return result

# Example usage
candidates1 = [2, 3, 6, 7]
target1 = 7
print(combinationSum(candidates1, target1))  # Output: [[2, 2, 3], [7]]

candidates2 = [2, 3, 5]
target2 = 8
print(combinationSum(candidates2, target2))  # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

candidates3 = [2]
target3 = 1
print(combinationSum(candidates3, target3))  # Output: []


"""#Explanation : for this brute force solution
# https://chatgpt.com/c/675fff42-2c34-8007-982d-369b7708c6c8"""

print("===========================================================")

#Solution 2:
def combinationSum2(candidates, target):
    def backtrack(start, path, remaining):
        # Base case: if the remaining sum is 0, add the path to the result
        if remaining == 0:
            result.append(path[:])  # Append a copy of the current path
            return
        # If the remaining sum is negative, stop exploring further
        if remaining < 0:
            return
        
        # Iterate through candidates starting from the current index
        for i in range(start, len(candidates)):
            # Include the current candidate
            path.append(candidates[i])
            # Recurse with updated remaining sum (unlimited usage allowed)
            backtrack(i, path, remaining - candidates[i])
            # Backtrack to explore other possibilities
            path.pop()
    
    result = []
    candidates.sort()  # Optional: Sorting helps to stop recursion earlier for some inputs
    backtrack(0, [], target)
    return result

# Example usage
candidates1 = [2, 3, 6, 7]
target1 = 7
print(combinationSum2(candidates1, target1))  # Output: [[2, 2, 3], [7]]

candidates2 = [2, 3, 5]
target2 = 8
print(combinationSum2(candidates2, target2))  # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

candidates3 = [2]
target3 = 1
print(combinationSum2(candidates3, target3))  # Output: []



print("===========================================================")


#Solution 3:
def combinationSum3( candidates, target):
        res = []
        candidates.sort()
        dfs(candidates, target, 0, [], res) 
        return res
    
def dfs(nums, target, index, path, res): 
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        dfs(nums, target-nums[i], i, path+[nums[i]], res)

"""
--->we optimze the DFS sol like this :

def combinationSum(candidates, target):
    def dfs(nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            dfs(nums, target - nums[i], i, path + [nums[i]], res)
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res
"""


# Example usage
candidates1 = [2, 3, 6, 7]
target1 = 7
print(combinationSum3(candidates1, target1))  # Output: [[2, 2, 3], [7]]

candidates2 = [2, 3, 5]
target2 = 8
print(combinationSum3(candidates2, target2))  # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

candidates3 = [2]
target3 = 1
print(combinationSum3(candidates3, target3))  # Output: []





"Resource:"
#https://www.w3schools.com/python/ref_list_pop.asp
#https://www.geeksforgeeks.org/python-list-pop-method/
#https://www.w3schools.com/python/ref_list_sort.asp
#https://www.geeksforgeeks.org/python-list-sort-method/
#https://www.geeksforgeeks.org/range-vs-xrange-in-python/

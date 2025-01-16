#problem
#https://leetcode.com/problems/combination-sum-ii/description/









#Solution 1:
def combinationSum2(candidates, target):
    def backtrack(start, path, current_sum):
        # Base case: if the current sum equals the target, add the path to results
        if current_sum == target:
            results.append(path[:])  # Add a copy of the current path
            return
        # Explore each number in the candidates
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i-1]:
                continue
            # Stop exploring if the current number makes the sum exceed the target
            if current_sum + candidates[i] > target:
                break
            # Choose the current number and continue the search
            path.append(candidates[i])
            backtrack(i + 1, path, current_sum + candidates[i])
            path.pop()  # Undo the choice (backtrack)
    
    candidates.sort()  # Sort to handle duplicates
    results = []
    backtrack(0, [], 0)
    return results

# Example Usage
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))



print("==========================================================")


#Solution 2 :
def combinationSumm(cand, target):
        cand.sort()
        res = []
        path = []
        dfs(cand, 0, target, path, res)
        return res
    
def dfs(cand, cur, target, path, res):
    if target == 0:
        res.append(path.copy())
        return
    if target < 0:
        return
    
    for i in range(cur, len(cand)):
        if i > cur and cand[i] == cand[i - 1]:  # Skip duplicates
            continue
        path.append(cand[i])
        dfs(cand, i + 1, target - cand[i], path, res)
        path.pop()  # Backtrack

# Example Usage
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSumm(candidates, target))

print("==========================================================")


#Explanation of the solutions
#https://chatgpt.com/c/67615eb4-7924-8007-a82f-a4ab8680415d
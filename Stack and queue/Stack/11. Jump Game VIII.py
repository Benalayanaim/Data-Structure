#Problem : https://leetcode.ca/2022-03-15-2297-Jump-Game-VIII/






#Solution 1:
from collections import defaultdict
def minCost(nums, costs):
    n = len(nums)
    g = defaultdict(list)
    stk = []
    for i in range(n - 1, -1, -1):
        while stk and nums[stk[-1]] < nums[i]:
            stk.pop()
        if stk:
            g[i].append(stk[-1])
        stk.append(i)

    stk = []
    for i in range(n - 1, -1, -1):
        while stk and nums[stk[-1]] >= nums[i]:
            stk.pop()
        if stk:
            g[i].append(stk[-1])
        stk.append(i)

    f = [float('inf')] * n
    f[0] = 0
    for i in range(n):
        for j in g[i]:
            f[j] = min(f[j], f[i] + costs[j])
    return f[n - 1]


nums = [3, 2, 4, 4, 1]
costs = [3, 7, 6, 4, 2]
print(minCost(nums, costs))  

nums = [0, 1, 2]
costs = [1, 1, 1]
print(minCost(nums, costs))  


print("===============================================")

#Solution 2:
def min_cost(nums, costs):

    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0  # The cost to reach the first index is 0

    for i in range(n):
        for j in range(i + 1, n):
            if (nums[i] <= nums[j] and all(nums[k] < nums[i] for k in range(i + 1, j))) or \
               (nums[i] > nums[j] and all(nums[k] >= nums[i] for k in range(i + 1, j))):
                dp[j] = min(dp[j], dp[i] + costs[j])

    return dp[-1]

# Example usage:
nums = [3, 2, 4, 4, 1]
costs = [3, 7, 6, 4, 2]
print(min_cost(nums, costs))  

nums = [0, 1, 2]
costs = [1, 1, 1]
print(min_cost(nums, costs)) 

""" Explanation:
    Returns the minimum cost to jump to the index n - 1.

    Args:
    nums (list): A 0-indexed integer array.
    costs (list): An integer array where costs[i] denotes the cost of jumping to index i.

    Returns:
    int: The minimum cost to jump to the index n - 1.
    """


print("===========================================================")

#Solution 3:
def minCost(nums, costs):
    n = len(nums)
    dp = [float('inf')] * n  # dp[i] represents the minimum cost to reach index i
    dp[0] = 0  # Starting point has no cost

    # Monotonic stacks
    increasing_stack = []  # To manage non-decreasing jumps
    decreasing_stack = []  # To manage decreasing jumps

    for i in range(n):
        # Process the increasing stack for valid non-decreasing jumps
        while increasing_stack and nums[increasing_stack[-1]] >= nums[i]:
            increasing_stack.pop()
        
        if increasing_stack:  # Top of the stack is the last valid jump index
            dp[i] = min(dp[i], dp[increasing_stack[-1]] + costs[i])

        # Process the decreasing stack for valid decreasing jumps
        while decreasing_stack and nums[decreasing_stack[-1]] <= nums[i]:
            decreasing_stack.pop()
        
        if decreasing_stack:  # Top of the stack is the last valid jump index
            dp[i] = min(dp[i], dp[decreasing_stack[-1]] + costs[i])

        # Push the current index onto both stacks
        increasing_stack.append(i)
        decreasing_stack.append(i)

    return dp[-1]

# Example usage:
nums = [3, 2, 4, 4, 1]
costs = [3, 7, 6, 4, 2]
print(min_cost(nums, costs))  

nums = [0, 1, 2]
costs = [1, 1, 1]
print(min_cost(nums, costs)) 



#Explanation : https://chatgpt.com/c/678f9629-c5ec-8006-86ee-a782c4cb3c4d
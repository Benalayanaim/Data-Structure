'Problem: '
#https://leetcode.com/problems/jump-game/



#Solution 1:
def canJump(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False  # If we can't reach this index, return False
        max_reach = max(max_reach, i + nums[i])  # Update the farthest reachable index
        if max_reach >= len(nums) - 1:
            return True  # If we can reach or exceed the last index, return True
    return False

# Test Case 1
print(canJump([2,3,1,1,5])) 

# Test Case 2
print(canJump([3,2,1,0,5]))  



print("===================================")
#Solution 2:
def canJump(nums):
    max_reach = 0
    for step in nums:
        if max_reach < 0:
            return False
        elif step > max_reach:
            max_reach = step
        max_reach -= 1
        
    return True
# Test Case 1
print(canJump([2,3,1,1,5])) 

# Test Case 2
print(canJump([3,2,1,0,5]))  



print("===================================")
#Solution 3:
def canJump(nums): 
        # Take curr variable to keep the current maximum jump...
        curr = nums[0]
        # Traverse all the elements through loop...
        for i in range(1,len(nums)):
            # If the current index 'i' is less than current maximum jump 'curr'...
            # It means there is no way to jump to current index...
            # so we should return false...
            if curr == 0:
                return False
            curr -= 1
            # Update the current maximum jump...
            curr = max(curr, nums[i])       # It’s possible to reach the end of the array...
        return True

# Test Case 1
print(canJump([2,3,1,1,5])) 

# Test Case 2
print(canJump([3,2,1,0,5])) 




print("===================================")
#Solution 4:
from typing import List

def canJump(nums: List[int]) -> bool:
    # If the array has only one element, we're already at the last index
    if len(nums) == 1:
        return True
    
    # Set the initial goal to the last index
    goal = len(nums) - 1

    # Iterate backward through the array starting from the second-to-last index
    for i in range(len(nums) - 2, -1, -1):
        # Check if we can jump to or beyond the current goal from index i
        if i + nums[i] >= goal:
            # Update the goal to the current index
            goal = i

    # If the goal reaches 0, return True, otherwise return False
    return goal == 0

# Test Case 1
print(canJump([2,3,1,1,5])) 

# Test Case 2
print(canJump([3,2,1,0,5])) 




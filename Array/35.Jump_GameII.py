"Problem"
#https://leetcode.com/problems/jump-game-ii/description/

#Solution 1:

def jump(nums):
    n = len(nums)
    if n == 1:
        return 0  
    
    jumps = 0 
    current_end = 0  
    farthest = 0  
    
    for i in range(n - 1):  # if We stop before the last element
        
        farthest = max(farthest, i + nums[i])
        
        
        if i == current_end:
            jumps += 1
            current_end = farthest  
    
    return jumps
nums = [2, 1, 2, 0, 1, 6]
print(jump(nums)) 

nums1 = [2, 3, 1, 1, 4]
print(jump(nums1))  


print("================================================")

"OR"

def jump(nums):
    n = len(nums)
    if n == 1:
        return 0  
    
    jumps = 0 
    current_end = 0  
    farthest = 0  
    
    for i in range(n):  # if We stop in the last element
        
        farthest = max(farthest, i + nums[i])
        
        
        if i == current_end:
            jumps += 1
            current_end = farthest  
            
            # If the farthest point reaches or exceeds the last index, we're done
            if current_end >= n - 1:
                break
    
    return jumps

nums = [2, 1, 2, 0, 1, 6]
print(jump(nums)) 

nums1 = [2, 3, 1, 1, 4]
print(jump(nums1))  



print("================================================")

#Solution N2:
def jump(nums): 
    start, reach, jumps = 0, 0, 0
    for i in range(len(nums) - 1):  # Iterate through the array except for the last index
        # Update the farthest point reachable
        if reach < nums[i] + i:
            reach = nums[i] + i
        
        # If we reach the boundary of the current jump range
        if i == start:
            start = reach  # Update the jump range
            jumps += 1  # Increment the jump counter
    
    return jumps

nums = [2, 1, 2, 0, 1, 6]
print(jump(nums)) 

nums1 = [2, 3, 1, 1, 4]
print(jump(nums1))  

print("==================================")


#Solution 3:
def jump(nums): 
        near = far = jumps = 0

        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            
            near = far + 1
            far = farthest
            jumps += 1
        
        return jumps

nums = [2, 1, 2, 0, 1, 6]
print(jump(nums)) 

nums1 = [2, 3, 1, 1, 4]
print(jump(nums1))  




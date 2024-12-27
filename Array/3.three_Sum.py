
#https://leetcode.com/problems/3sum/solutions/6043935/explained-using-three-approaches-hashmap-two-pointers/




def threeSum(nums):
    nums.sort()  # Sort the array to handle duplicates and use two pointers
    result = []
    
    for i in range(len(nums)):
        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointers for the remaining array
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Move left and right pointers to avoid duplicates
                left += 1
                right -= 1
                
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            
            elif total < 0:
                left += 1  # Increase the sum
            else:
                right -= 1  # Decrease the sum
    
    return result



nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))


#Solution N 2
def threeSum(numss):
        result = set()
        numss.sort()
        for i in range(len(numss)):
            for j in range(i+1, len(numss)):
                for k in range(j+1, len(numss)):
                    if numss[i] + numss[j] + numss[k] == 0:
                        result.add((numss[i], numss[j], nums[k]))
        return [triplet for triplet in result]
numss = [-1,0,1,2,-1,-4]
print(threeSum(numss))



#another solution : https://leetcode.com/problems/3sum/solutions/6043935/explained-using-three-approaches-hashmap-two-pointers/
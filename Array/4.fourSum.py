
#https://leetcode.com/problems/4sum/description/


#Solution 3 :
def fourSum(nums, target):
    nums.sort()
    results = []
    helper(nums, target, 4, [], results)
    return results

def helper(nums, target, N, res, results):
    
    if len(nums) < N or N < 2: #1
        return
    if N == 2: #2
        output_2sum =twoSum(nums, target)
        if output_2sum != []:
            for idx in output_2sum:
                results.append(res + idx)
    
    else: 
        for i in range(len(nums) - N +1): #3
            if nums[i]*N > target or nums[-1]*N < target: #4
                break
            if i == 0 or i > 0 and nums[i-1] != nums[i]: #5
                helper(nums[i+1:], target-nums[i], N-1, res + [nums[i]], results)


def twoSum(nums, target):
    res = []
    left = 0
    right = len(nums) - 1 
    while left < right: 
        temp_sum = nums[left] + nums[right] 

        if temp_sum == target:
            res.append([nums[left], nums[right]])
            right -= 1
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while right > left and nums[right] == nums[right + 1]:
                right -= 1
                            
        elif temp_sum < target: 
            left +=1 
        else: 
            right -= 1
                                    
    return res

# Example usage
nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
print(fourSum(nums1, target1))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

nums2 = [2, 2, 2, 2, 2]
target2 = 8
print(fourSum(nums2, target2))  # Output: [[2, 2, 2, 2]]

"""Explanation
https://leetcode.com/problems/4sum/solutions/737096/sum-megapost-python3-solution-with-a-detailed-explanation/"""


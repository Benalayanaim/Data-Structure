#Problem 
#https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=array





#Solution 1: def minSubArrayLen(target, nums):
def minSubArrayLen(target, nums):
    min_length = float('inf')
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0

target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))

target = 4
nums = [1, 4, 4]
print(minSubArrayLen(target, nums))

target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
print(minSubArrayLen(target, nums))




#Explanation : https://chat.deepseek.com/a/chat/s/477252bc-aeb8-43cd-af73-9c5dd4d818ef

#https://chatgpt.com/c/67a37805-47e4-800f-bf1f-d9c38cc7ea35
#Problem
#https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=problem-list-v2&envId=array



#Solution 1:
def findMaxAverage(nums, k):
    # Calculate the sum of the first 'k' elements
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Iterate through the array starting from the k-th element
    for i in range(k, len(nums)):
        # Slide the window: subtract the element going out and add the new element
        window_sum += nums[i] - nums[i - k]
        # Update the maximum sum if the current window sum is greater
        max_sum = max(max_sum, window_sum)
    
    # Calculate the maximum average
    max_average = max_sum / k
    return max_average

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))

nums = [5]
k = 1
print(findMaxAverage(nums, k))


"""Explanation :
==>https://leetcode.com/problems/maximum-average-subarray-i/solutions/3532127/py3-beginner-friendly-with-details-and-explanation/?envType=problem-list-v2&envId=array"""


print("===========================================")

#Solution 2:
def findMaxAverage(nums, k):
    # take first k elements -> get average
        # loop one by one -> delete i-n element-> take current max
        curr_sum = 0
        for i in range(k):
            curr_sum = curr_sum + nums[i]

        max_sum = curr_sum
        for i in range(k, len(nums)):
            curr_sum = curr_sum - nums[i - k] + nums[i]
            max_sum = max(curr_sum, max_sum)
            
        return max_sum / k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))

nums = [5]
k = 1
print(findMaxAverage(nums, k))




print("===========================================")

#Solution 2:
def findMaxAverage(nums, k): 
    total = sum(nums[:k])
    maxAvg = total/k

    for i in range(len(nums)-k):#for keep traking the element after (nums[:k])
        total -= nums[i]
        total += nums[i+k]
        maxAvg = max(maxAvg, total/k)

    return maxAvg

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))

nums = [5]
k = 1
print(findMaxAverage(nums, k))






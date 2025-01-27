#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/


#Solution 1:
def findDisappearedNumbers(nums):
    # Mark elements as negative to indicate presence
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])

    # Collect the indices with positive values, which correspond to missing numbers
    result = [i + 1 for i in range(len(nums)) if nums[i] > 0]

    return result
nums = [0,2,2,1,1]  
print(findDisappearedNumbers(nums))


print("==============")


#Solution 2:
def FinAllDisappearNumbers(nums):
    for i in range(len(nums)):
        # Only process indices within the valid range
        if 1 <= abs(nums[i]) <= len(nums):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1

    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)

    return res

nums = [0,2,2,1,1]  
print(FinAllDisappearNumbers(nums))



print("==============")

#Solution 3
def FinAllDisappearNumbers(nums):
    return [i for i in range(1, len(nums)+1) if i not in nums]


nums = [0,2,2,1,1] # 6 is out of range
print(FinAllDisappearNumbers(nums))




#Explanation : https://www.youtube.com/watch?v=wx1jbjpPbF4&list=PLElbz74hCXjQxCcd6dscrXviVH5e2lLcf&index=1

#Explanation another : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/solutions/1583736/c-python-all-6-solutions-w-explanations-binary-search-hashset-2x-o-1-space-approach/


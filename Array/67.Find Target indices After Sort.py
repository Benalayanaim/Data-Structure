#Problem : https://leetcode.com/problems/find-target-indices-after-sorting-array/description/?envType=problem-list-v2&envId=array





#Solution 1:
def targetIndices(nums, target):
        ans = []
        for i,num in enumerate(sorted(nums)):
            if num == target: ans.append(i)
        return ans

#Example Usage
nums = [1,2,5,2,3]
target = 2
print(targetIndices(nums, target))

nums = [1,2,5,3]
target = 3
print(targetIndices(nums, target))

nums = [1,2,5,2,3]
target = 10
print(targetIndices(nums, target))

print("===========================================================")

#Solution 2:
def targetIndices(nums, target):
        return [i for i,num in enumerate(sorted(nums)) if num==target]

#Example Usage
nums = [1,2,5,2,3]
target = 2
print(targetIndices(nums, target))

nums = [1,2,5,3]
target = 3
print(targetIndices(nums, target))

nums = [1,2,5,2,3]
target = 10
print(targetIndices(nums, target))






print("===========================================================")

#Solution 3:
def targetIndices(nums, target):
    nums.sort()   
    result = []
    for i in range(len(nums)):
        if nums[i] == target:
            result.append(i)
    
    return result

#Example Usage
nums = [1,2,5,2,3]
target = 2
print(targetIndices(nums, target))

nums = [1,2,5,3]
target = 3
print(targetIndices(nums, target))

nums = [1,2,5,2,3]
target = 10
print(targetIndices(nums, target))


print("===========================================================")

#Solution 4:
def targetIndices(nums, target):
    l1=sorted(nums)
    l2=[]
    for i in range(len(l1)):
        if target==l1[i]:
            l2.append(i)
    return l2

#Example Usage
nums = [1,2,5,2,3]
target = 2
print(targetIndices(nums, target))

nums = [1,2,5,3]
target = 3
print(targetIndices(nums, target))

nums = [1,2,5,2,3]
target = 10
print(targetIndices(nums, target))
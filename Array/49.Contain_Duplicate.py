#https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=array





"Brute Force"
#Solution 1:

def containsDuplicate(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


nums1 = [1,2,3,1]
nums2 = [1,2,3,4]


print(containsDuplicate(nums1))
print(containsDuplicate(nums2))


print("==========================")

"Sorting"
#Solution 2:
def containsDuplicate(nums):
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False


nums1 = [1,2,3,1]
nums2 = [1,2,3,4]


print(containsDuplicate(nums1))
print(containsDuplicate(nums2))


print("==========================")

"Hash Set"
#Solution 3:

def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

nums1 = [1,2,3,1]
nums2 = [1,2,3,4]


print(containsDuplicate(nums1))
print(containsDuplicate(nums2))

print("==========================")

"Hash Map"
#Solution 4:
def containsDuplicate(nums):
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False

nums1 = [1,2,3,1]
nums2 = [1,2,3,4]


print(containsDuplicate(nums1))
print(containsDuplicate(nums2))

"this explanation to understand the last solution :"
"Fy chat mteiiii"
#Explanation : https://chatgpt.com/c/6783d39f-49e8-800f-9650-7c381a10e5df


print("===================================")

#Solution5
def containsDuplicate(nums):

    if len(nums) == len(set(nums)):
                return False
    return True

nums1 = [1,2,3,1]
nums2 = [1,2,3,4]


print(containsDuplicate(nums1))
print(containsDuplicate(nums2))
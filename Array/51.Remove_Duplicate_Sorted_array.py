#Problem
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=problem-list-v2&envId=array






#Solution 1:
def removeDuplicates(nums):
    if not nums:
        return 0
    
    # Initialize a pointer for the position of unique elements
    unique_index = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]
    
    # The number of unique elements is unique_index + 1
    return unique_index + 1

# Example usage
nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

k1 = removeDuplicates(nums1)
k2 = removeDuplicates(nums2)

print(k1, nums1[:k1])  
print(k2, nums2[:k2])  


print("=================================================")

#Solution 2:
def removeDuplicates1(nums):
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k

# Example usage
nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(removeDuplicates1(nums1))
print(removeDuplicates1(nums2))


print("=================================================")

#Solution 3:
def removeDuplicates2(nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)  # Remove duplicate
            else:
                i += 1
        return len(nums)

# Example usage
nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(removeDuplicates2(nums1))
print(removeDuplicates2(nums2))




print("=================================================")

#Solution 4:
def removeDuplicates3(nums):
        lst=[]
        k=0
        for num in nums:    
            if num not in lst:
                lst.append(num)
                nums[k]=num
                k+=1
        return k


# Example usage
nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(removeDuplicates3(nums1))
print(removeDuplicates3(nums2))




"Explanation : https://chatgpt.com/c/6784f3ee-71dc-800f-bcbd-c684e2c914d7"
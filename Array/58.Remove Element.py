#Problem : https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array







#Solution 1:
def removeElement(nums, val) -> int:
        i = 0  # Pointer for iterating through the list
        while i < len(nums):
            if nums[i] == val:
                #del nums[i]  # Remove the element if it matches `val`
                nums.pop(i)
            else:
                i += 1  # Move to the next element only if no deletion occurs
        return len(nums)



nums1 = [3,2,2,3] 
val1 = 3
print(removeElement(nums1, val1))


nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
print(removeElement(nums2, val2))

print("=====================================================")
#Solution 2
def removeElement(nums, val):
    k = 0  # Pointer for the position of elements not equal to `val`
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


nums1 = [3,2,2,3] 
val1 = 3
print(removeElement(nums1, val1))


nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
print(removeElement(nums2, val2))


print("=====================================================")
#Solution 3:
def removeElement(nums, val):
 while val in nums:
            nums.remove(val)
 return len(nums) 

nums1 = [3,2,2,3] 
val1 = 3
print(removeElement(nums1, val1))


nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
print(removeElement(nums2, val2))



#Probelm
#https://leetcode.com/problems/single-element-in-a-sorted-array/description/?envType=problem-list-v2&envId=array



#Solution 1:

def singleNonDuplicate(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # Ensure mid is even
        if mid % 2 == 1:
            mid -= 1
        
        # Check if the pair is intact
        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid
    
    return nums[left]


nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))

nums = [3,3,7,7,10,11,11]
print(singleNonDuplicate(nums))


#Explanation : https://chat.deepseek.com/a/chat/s/084c3387-e158-4487-a8b2-3c0f8049a455

print("============================================")

#Solution 2:
from collections import Counter
def singleNonDuplicate(nums) -> int:
        
        count_num = Counter(nums)
        for num, freq in count_num.items():
            if freq == 1:
                return num


nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))

nums = [3,3,7,7,10,11,11]
print(singleNonDuplicate(nums))
            

print("============================================")

#Solution 3:
def singleNonDuplicate(nums) -> int:
        n=len(nums)
        i=0
        while i<n-1:
            if (nums[i]==nums[i+1]) or (nums[i]==nums[i-1]):
                i+=1
            else:
                return nums[i]
        return nums[-1]

nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))

nums = [3,3,7,7,10,11,11]
print(singleNonDuplicate(nums))
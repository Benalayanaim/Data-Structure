#Problem:
#https://leetcode.com/problems/majority-element-ii/?envType=problem-list-v2&envId=array







"HashMap Approach"


#Solution 1:

from collections import Counter
def majorityElement(nums: list[int]) -> list[int]:
        # Create a Counter to store the count of each element
        element_count = Counter(nums)
        
        majority_elements = []
        threshold = len(nums) // 3
        
        # Iterate through the element count to identify majority elements
        for element, count in element_count.items():
            # Check if the element count is greater than the threshold
            if count > threshold:
                majority_elements.append(element)
        
        return majority_elements


#Example Usage
nums = [3,2,3]
print(majorityElement(nums))

nums = [1]
print(majorityElement(nums))

nums = [1,2]
print(majorityElement(nums))


print("==============================================")


#Solution 
from collections import defaultdict
def majorityElement(nums: list[int]) -> list[int]:
        occ = defaultdict(int)
        for n in nums:
            occ[n]+=1
        maj = []
        for k in occ:
            if occ[k] > len(nums) / 3:
                maj.append(k)
        return maj


#Example Usage
nums = [3,2,3]
print(majorityElement(nums))

nums = [1]
print(majorityElement(nums))

nums = [1,2]
print(majorityElement(nums))

print("==============================================")


#Solution 

def majorityElement(nums: list[int]) -> list[int]:
        occ = {}
        for n in nums:
            if n in occ:
                occ[n]+=1
            else:
                 occ[n]=1
        maj = []
        for k in occ:
            if occ[k] > len(nums) / 3:
                maj.append(k)
        return maj


#Example Usage
nums = [3,2,3]
print(majorityElement(nums))

nums = [1]
print(majorityElement(nums))

nums = [1,2]
print(majorityElement(nums))


print("==============================================")


#Solution 
def majorityElement(nums):
        n = len(nums)
        res = []
        for d in set(nums):
            if nums.count(d) > n // 3:
                res.append(d)
        return res


#Example Usage
nums = [3,2,3]
print(majorityElement(nums))

nums = [1]
print(majorityElement(nums))

nums = [1,2]
print(majorityElement(nums))

#Problem 
#https://leetcode.com/problems/majority-element/description/?envType=problem-list-v2&envId=array



"Hash Map"
#Solution 1:
from collections import defaultdict
def majorityElement(nums) -> int:
        n = len(nums)
        m = defaultdict(int)
        
        for num in nums:
            m[num] += 1
        
        n = n // 2
        for key, value in m.items():
            if value > n:
                return key
        
        return 0

nums = [3,2,3]
print(majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))



print("======================================")

#Solution 2:
def majorityElement(nums) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
            if counter[num] > len(nums) // 2: return num
        return None

nums = [3,2,3]
print(majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))

print("======================================")

#Solution 2:
def majorityElement(nums) -> int:
        res = maxim = 0
        dct = {}

        for num in nums:
            if num not in dct:
                dct[num] = 1
            else:
                dct[num] += 1
                
            if dct[num] > maxim:
                maxim = dct[num]
                res = num
                
        return res

nums = [3,2,3]
print(majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))


print("======================================")

from collections import Counter
#Solution 3:
def majorityElement(nums) -> int:
        counters = Counter(nums)
        for num, count in counters.items():
            if count > len(nums) // 2: return num
        return None

nums = [3,2,3]
print(majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))


print("======================================")

#Solution 4:
def majorityElement(nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]

nums = [3,2,3]
print(majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))


print("======================================")
"Approach : Moore Voting Algorithm"

#Solution 5:
def majorityElement(nums):
        counter = 0
        majority_number = 0

        for num in nums:
            if counter == 0:
                majority_number = num

            if majority_number == num:
                counter += 1
            else:
                counter -= 1
        
        return majority_number

nums = [3,2,3]
print(majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))



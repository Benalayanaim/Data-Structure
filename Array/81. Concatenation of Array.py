#Prolem
#https://leetcode.com/problems/concatenation-of-array/description/?envType=problem-list-v2&envId=array





#Solution 1:

def getConcatenation(nums) :
        result = []
        for num in nums:
            result.append(num)  # Add each element from nums
        for num in nums:
            result.append(num)  # Add each element again
        return result

nums = [1,2,1]
print(getConcatenation(nums))

nums = [1,3,2,1]
print(getConcatenation(nums))
"""Approach:
1/Start with an empty list called result.
2/Loop through the original list and append each element to result.
3/Loop through the original list again and append each element to result.
4/Return the result list."""

print("============================================")

#Solution 2:
def getConcatenation(nums):
        n = len(nums)
        result = [0] * (2 * n)  # Create a new list of size 2n
        for i in range(n):
            result[i] = nums[i]      # Copy the first part
            result[i + n] = nums[i]  # Copy the second part
        return result

nums = [1,2,1]
print(getConcatenation(nums))

nums = [1,3,2,1]
print(getConcatenation(nums))

"""Approach:
Determine the length of the original list.
Create a new list called result with twice the length of the original list.
Use a loop to set each element in the new list:
First, copy elements from the original list.
Then, copy elements from the original list again, starting at the next index.
Return the result list."""

#The difference between result = [0] * (2 * n) and result = [] * (2 * n)
#https://chat.deepseek.com/a/chat/s/52c4ad42-131e-4779-a380-aab9bc9c98f7


print("============================================")

#Solution 2:
def getConcatenation(nums):
        n = len(nums)
        result = [0] * (2 * n)  # Create a new list of size 2n
        for i, num in enumerate(nums):
            result[i] = num         # Copy the first part
            result[i + n] = num     # Copy the second part
        return result

nums = [1,2,1]
print(getConcatenation(nums))

nums = [1,3,2,1]
print(getConcatenation(nums))

"""Approach:
Determine the length of the original list.
Create a new list called result with twice the length of the original list.
Use a loop to set each element in the new list:
First, copy elements from the original list.
Then, copy elements from the original list again, starting at the next index.
Return the result list."""


print("============================================")

#Solution 2:
def getConcatenation(nums):
        ans = nums[:] #copy from the origin
        for i in nums:
            ans.append(i)
        return ans

nums = [1,2,1]
print(getConcatenation(nums))

nums = [1,3,2,1]
print(getConcatenation(nums))




print("============================================")

#Solution 2:
def getConcatenation(nums):
        nums.extend(nums)  # Extend the list with itself
        return nums     

nums = [1,2,1]
print(getConcatenation(nums))

nums = [1,3,2,1]
print(getConcatenation(nums))



print("============================================")

#Solution 2:
def getConcatenation(nums):
         return nums + nums  # Concatenate the list with itself
         #return nums * 2  # Repeat the list twice
nums = [1,2,1]
print(getConcatenation(nums))

nums = [1,3,2,1]
print(getConcatenation(nums))

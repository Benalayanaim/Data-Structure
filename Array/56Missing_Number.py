#Problem : https://chatgpt.com/c/678e529c-6fd8-800f-86f8-3d3c79eee374




#Solution 1:
def missingNumber(nums):
    n = len(nums)  # The range is [0, n]
    for i in range(n + 1):  # Iterate over all numbers from 0 to n
        if i not in nums:  # Check if i is not in the array
            return i  # Return the missing number

# Test cases
print(missingNumber([3, 0, 1]))  
print(missingNumber([0, 1]))  
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  




print("=======================================")
#Solution 2:
def missingNumber(nums):

        res = len(nums)
        nums.sort()
        for i in range(len(nums)): 
            res += i - nums[i]

        return res 

# Test cases
print(missingNumber([3, 0, 1]))  
print(missingNumber([0, 1]))  
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  




print("=======================================")
#Solution 2:
def missingNumber( nums):
        nums.sort()
        # print(nums)
        for i, j in zip(nums, range(len(nums)+1)): 
            #print(i, j)
            if i != j:
                return j
        return len(nums)

# Test cases
print(missingNumber([3, 0, 1]))  
print(missingNumber([0, 1]))  
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  




print("=======================================")
#Solution 2:
def missingNumber(nums):
        n = len(nums)
        nums.sort()
        for i in range(0,n):
            if i not in nums :
                return i
        return n

# Test cases
print(missingNumber([3, 0, 1]))  
print(missingNumber([0, 1]))  
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  



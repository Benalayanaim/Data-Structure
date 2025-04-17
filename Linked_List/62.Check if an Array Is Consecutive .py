#Problem 
#https://leetcode.ca/2022-05-01-2229-Check-if-an-Array-Is-Consecutive/
#https://leetcodethehardway.com/solutions/2200-2299/check-if-an-array-is-consecutive-easy
#https://www.youtube.com/watch?v=SyRzsfmS__M








""""The brute force solution involves checking each number in the range 
from the minimum value `x` to `x + n - 1` (inclusive) to see if it exists in the array `nums`.
"""
#Solution1:
def is_consecutive(nums):

    # Calculate the minimum value and the length of the array
    min_val = min(nums)
    n = len(nums)

    # Check each number in the range [x, x + n - 1] to see if it exists in nums
    for num in range(min_val, min_val + n):
        if num not in nums:
            # If any number in the range does not exist in nums, return False
            return False

    # If all numbers in the range exist in nums, return True
    return True


# Example usage:
nums = [1, 3, 4, 2]
print(is_consecutive(nums))  

nums = [1, 3]
print(is_consecutive(nums)) 


nums = [5,4, 3]
print(is_consecutive(nums)) 

### Explanation
"""
1.  Find the minimum value in the array `nums` using the `min` function and store it in `min_val`.
2.  Calculate the length of the array `nums` and store it in `n`.
3.  Use a for loop to iterate through the range from `min_val` to `min_val + n - 1` (inclusive).
4.  Inside the loop, check if each number `i` in the range exists in the array `nums` using the `in` operator.
5.  If any number `i` in the range does not exist in `nums`, immediately return `False`, indicating that `nums` is not consecutive.
6.  If the loop completes without finding any missing numbers, return `True`, indicating that `nums` is consecutive.
"""



print("============================================================")
#Solution 2:
def is_consecutive(nums):
    # Convert the list to a set for O(1) lookups
    num_set = set(nums)

    # Calculate the minimum value and the length of the array
    min_val = min(nums)
    n = len(nums)

    # Check each number in the range [x, x + n - 1] to see if it exists in num_set
    for i in range(min_val, min_val + n):
        if i not in num_set:
            # If any number in the range does not exist in num_set, return False
            return False

    # If all numbers in the range exist in num_set, return True
    return True


# Example usage:
nums = [1, 3, 4, 2]
print(is_consecutive(nums))  

nums = [1, 3]
print(is_consecutive(nums)) 

nums = [5,4, 3]
print(is_consecutive(nums)) 

### Explanation
"""
1.  Convert the list `nums` to a set `num_set` using the `set` function, which allows for O(1) lookups.
2.  Find the minimum value in the array `nums` using the `min` function and store it in `min_val`.
3.  Calculate the length of the array `nums` and store it in `n`.
4.  Use a for loop to iterate through the range from `min_val` to `min_val + n - 1` (inclusive).
5.  Inside the loop, check if each number `i` in the range exists in the set `num_set` using the `in` operator.
6.  If any number `i` in the range does not exist in `num_set`, immediately return `False`, indicating that `nums` is not consecutive.
7.  If the loop completes without finding any missing numbers, return `True`, indicating that `nums` is consecutive.
"""


print("============================================================")
#Solution 3:
def is_consecutive(nums):
    # Convert the list to a set for O(1) lookups
    num_set = set(nums)

    # Check if the length of the set is equal to the length of the array
    if len(num_set) != len(nums):
        return False

    # Calculate the minimum value and the length of the array
    min_val = min(nums)
    n = len(nums)

    # Check each number in the range [x, x + n - 1] to see if it exists in num_set
    for i in range(min_val, min_val + n):
        if i not in num_set:
            # If any number in the range does not exist in num_set, return False
            return False

    # If all numbers in the range exist in num_set, return True
    return True


# Example usage:
nums = [1, 3, 4, 2]
print(is_consecutive(nums))  

nums = [1, 3]
print(is_consecutive(nums)) 


nums = [5,4, 3]
print(is_consecutive(nums)) 

"""
This optimized solution has the same time complexity of O(n), but it is more robust as it handles the case where the input array
 has duplicate elements.
"""


print("============================================================")
#Solution 4:
def is_consecutive(nums):
    # Get the minimum value and the maximum value in the array
    min_val = min(nums)
    max_val = max(nums)
    
    # Check if the difference between max and min equals the length of nums - 1
    if max_val - min_val != len(nums) - 1:
        return False
    
    # Check if all numbers in the range are present
    return set(nums) == set(range(min_val, max_val + 1))


# Example usage:
nums = [1, 3, 4, 2]
print(is_consecutive(nums))  

nums = [1, 3]
print(is_consecutive(nums)) 


nums = [5,4, 3]
print(is_consecutive(nums)) 

#Explanation for the last solution : https://chatgpt.com/c/6790fecb-9418-800f-87de-dc1ae7c5b37f

#Problem 
#https://leetcode.com/problems/contiguous-array/?envType=problem-list-v2&envId=array








"Brute force "

#Solution 1:
def findMaxLength(nums):

    max_length = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = nums[i:j+1]
            zeros = subarray.count(0)
            ones = subarray.count(1)
            if zeros == ones:
                max_length = max(max_length, len(subarray))
    return max_length

# Example usage
print(findMaxLength([0,1]))  
print(findMaxLength([0,1,0]))  
print(findMaxLength([0,1,0,1]))
print(findMaxLength([0,1,1,1,0,1,0,1]))

"IF you need more Clarifiaction try to do with Python Complier"
#Explanation :
"""**Explanation**

1.  We initialize `max_length` to 0, which will store the maximum length of a contiguous subarray with an equal number of 0 and 1.
2.  We use two nested loops to generate all possible subarrays of `nums`.
3.  For each subarray, we count the number of 0s and 1s using the `count` method.
4.  If the number of 0s and 1s is equal, we update `max_length` if the length of the current subarray is greater than `max_length`.
5.  Finally, we return `max_length`, which is the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""



print("===========================================================")


#Solution 1:
def findMaxLength(nums):
    count = 0  # Running sum
    hash_map = {0: -1}  # Store first occurrence of a count
    max_length = 0

    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1  # Convert 0 to -1

        if count in hash_map:
            max_length = max(max_length, i - hash_map[count])
        else:
            hash_map[count] = i  # Store first occurrence of this count

    return max_length


# Example usage
print(findMaxLength([0,1]))  
print(findMaxLength([0,1,0]))  
print(findMaxLength([0,1,0,1]))
print(findMaxLength([0,1,1,1,0,1,0,1]))




print("===========================================================")


#Solution 1:
def findMaxLength(nums):
    count = 0
    hash_map = {}  # No {0: -1}
    max_length = 0

    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1

        if count in hash_map:
            max_length = max(max_length, i - hash_map[count])
        else:
            hash_map[count] = i

    return max_length

print(findMaxLength([0, 1]))  # Output: 0 (Incorrect!)



# Example usage
print(findMaxLength([0,1]))  
print(findMaxLength([0,1,0]))  
print(findMaxLength([0,1,0,1]))
print(findMaxLength([0,1,1,1,0,1,0,1]))


print("===========================================================")


#Solution 1:

def findMaxLength(nums):
    # Initialize a hash map to store the first occurrence of each prefix sum
    prefix_map = {0: -1}
    max_len = 0
    prefix_sum = 0

    for i in range(len(nums)):
        # Treat 0 as -1 and 1 as +1
        if nums[i] == 0:
            prefix_sum -= 1
        else:
            prefix_sum += 1

        # If the prefix sum is already in the map, update the maximum length
        if prefix_sum in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum])
        else:
            # Otherwise, store the current index for this prefix sum
            prefix_map[prefix_sum] = i

    return max_len


# Example usage
print(findMaxLength([0,1]))  
print(findMaxLength([0,1,0]))  
print(findMaxLength([0,1,0,1]))
print(findMaxLength([0,1,1,1,0,1,0,1]))

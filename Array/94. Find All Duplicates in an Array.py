#Problem
#https://leetcode.com/problems/find-all-duplicates-in-an-array/description/?envType=problem-list-v2&envId=array


#Solution:

def findDuplicates(nums):
        seen = set()
        dup = []
        for i in nums:
            if i in seen:
                dup.append(i)
            else:
                seen.add(i)
        return dup

print("==============================================")

#Solution :2
def findDuplicates(nums):
    dic = {}

    for num in nums:
     if num in dic:
         dic[num] += 1
     else :
        dic[num] = 1
    
    res = []
    for num, val in dic.items():
        if val == 2:
            res.append(num)
    return res



print("==============================================")

#Solution :2
def findDuplicates(nums):

        output = []
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0)+1

        output = [num for num in hash if hash[num] == 2]
        return output


print("==============================================")

#Solution :2
def findDuplicates(nums):
    zero = [0] * len(nums)  # Initialize a zero array of size n
    res = []  # Result list to store duplicates
    for num in nums:
        index = num - 1  # Calculate the index for the current number
        if zero[index] == 1:  # If the number has been seen before
            res.append(num)  # Add it to the result list
        else:
            zero[index] = 1  # Mark the number as seen
    return res

"""Explanation
1/ Initialize an array zero of size n with all elements set to 0.

2/ Iterate through each number in nums.

3/ or each number num, calculate its corresponding index in the zero array as index = num - 1.

4/ If zero[index] is already 1, it means the number num has been seen before, so it is a duplicate. Append it to the result list res.

5/ If zero[index] is 0, set it to 1 to mark that the number has been seen.

6/ Return the result list res.
"""

#Problem : 
# https://www.youtube.com/watch?v=69oSP_KyYEw&t=115s
# https://leetcode.ca/2017-12-29-760-Find-Anagram-Mappings/







#Solution 1:
def anagramMappings(nums1, nums2):
    mapping = []
    for num in nums1:
        for i in range(len(nums2)):
            if nums2[i] == num:
                mapping.append(i)
                break
    return mapping

# Example usage:
nums1 = [12, 28, 46, 32, 50]
nums2 = [50, 12, 32, 46, 28]
print(anagramMappings(nums1, nums2))  

nums1 = [84, 46]
nums2 = [84, 46]
print(anagramMappings(nums1, nums2))  



print("====================================================================")

#Solution 2:
def anagram_mapping(nums1, nums2):

    # Create a dictionary to store the index of each element in nums2
    index_dict = {val: idx for idx, val in enumerate(nums2)}

    # Create the mapping array by looking up the index of each element in nums1
    mapping = [index_dict[val] for val in nums1]

    return mapping

# Example usage:
nums1 = [12, 28, 46, 32, 50]
nums2 = [50, 12, 32, 46, 28]
print(anagramMappings(nums1, nums2))  

nums1 = [84, 46]
nums2 = [84, 46]
print(anagramMappings(nums1, nums2))  

"""Explanation:

    Returns an index mapping array from nums1 to nums2.

    Args:
    nums1 (list): The first integer array.
    nums2 (list): The second integer array, which is an anagram of nums1.

    Returns:
    list: An index mapping array mapping from nums1 to nums2.
"""

print("====================================================================")

#Solution 3:

from collections import defaultdict

def anagramMappings(nums1, nums2):
        mapper = defaultdict(set)
        for i, num in enumerate(nums2):
            mapper[num].add(i)
        return [mapper[num].pop() for num in nums1]

# Example usage:
nums1 = [12, 28, 46, 32, 50]
nums2 = [50, 12, 32, 46, 28]
print(anagramMappings(nums1, nums2))  

nums1 = [84, 46]
nums2 = [84, 46]
print(anagramMappings(nums1, nums2))  



#Explanation : https://chatgpt.com/c/678f7412-f6c0-800f-aa47-163e36720831
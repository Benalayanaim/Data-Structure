"Problem"
#https://leetcode.com/problems/contains-duplicate-ii/submissions/1506291966/?envType=problem-list-v2&envId=array


"Brute Force"

#Solution 2:
def containsNearbyDuplicate(nums, k):

    # Iterate over all pairs of indices i and j
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False

nums1 = [1,2,3,1]
k1 = 3
nums2 = [1,2,3,1,2,3]
k2 = 2

print(containsNearbyDuplicate(nums1, k1))
print(containsNearbyDuplicate(nums2, k2))


print("========================================")


"Hashmap"
#Solution 2:

def containsNearbyDuplicate(nums, k):
    # Create a dictionary (hset) to store elements and their last seen index.
    hset = {}
    
    # Iterate through the array with index 'idx'.
    for idx in range(len(nums)):
        
        # Check if the element is already in the dictionary and if the distance between indices is <= k.
        if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
            return True
        
        # Store the current element and its index in the dictionary.
        hset[nums[idx]] = idx
    
    # If no valid pair is found, return False.
    return False


nums1 = [1,2,3,1]
k1 = 3
nums2 = [1,2,3,1,2,3]
k2 = 2

print(containsNearbyDuplicate(nums1, k1))
print(containsNearbyDuplicate(nums2, k2))


print("========================================")


"Hashmap"
#Solution 3:

def containsNearbyDuplicate(nums, k):
    seen = {}  # Dictionary to store the element and its last seen index.
    
    # Iterate over the list `nums` with index `i` and value `val`.
    for i, val in enumerate(nums):
        
        # Check if the element has been seen before and if the difference in indices is <= k.
        if val in seen and i - seen[val] <= k:
            return True  # Found a duplicate within the range, return True.
        else:
            # Store the index of the current element.
            seen[val] = i
    
    # If no such duplicate is found, return False.
    return False

nums1 = [1,2,3,1]
k1 = 3
nums2 = [1,2,3,1,2,3]
k2 = 2

print(containsNearbyDuplicate(nums1, k1))
print(containsNearbyDuplicate(nums2, k2))


"Fy chat mteiiii"
#Explanation : https://chatgpt.com/c/6783d8de-0048-800f-83ae-cd39b4aa32b5
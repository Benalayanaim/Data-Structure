#Problem
#https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=problem-list-v2&envId=array






#Solution 1:
from collections import Counter

def intersect(nums1, nums2):

    # Step 1: Count occurence of each element in nums1
    count_nums1 = Counter(nums1)
    result = []
    
    
    #Step 2: Iterate over nums2 and find common elements
    for num in nums2:
        # Check the element is in count_nums1 and its count is more than 0
        if count_nums1[num] >0:
            result.append(num) #Add it to the result
            
            count_nums1[num] -= 1 #decrement the count in count_nums
            
    return result

nums1 = [1,2,2,1] 
nums2 = [2,2,3]
print(intersect(nums1, nums2))


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))

print("===============================================================")

#Solution 2:
def intersection(nums1, nums2):
        res = []
        curr_array = nums1
        other_array = nums2

        for num in curr_array:
            if num in other_array:
                res.append(num)
                other_array.remove(num)

        return res

nums1 = [1,2,2,1] 
nums2 = [2,2,3]
print(intersection(nums1, nums2))


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))


print("===============================================================")

#Solution 3:

def intersection(nums1, nums2):
        # Sort both the arrays first...
        sortedArr1 = sorted(nums1)
        sortedArr2 = sorted(nums2)
        # Use two pointers i and j for the two arrays and initialize both with zero.
        i = 0
        j = 0
        # Create a output list to store the output...
        output = []
        while i < len(sortedArr1) and j < len(sortedArr2):
            # If sortedArr1[i] is less than sortedArr2[j]...
            # Leave the smaller element and go to next(greater) element in nums1...
            if sortedArr1[i] < sortedArr2[j]:
                i += 1
            # If sortedArr1[i] is greater than sortedArr2[j]...
            # Go to next(greater) element in nums2 array...
            elif sortedArr2[j] < sortedArr1[i]:
                j += 1
            # If both the elements intersected...
            # Add this element to output & increment both i and j.
            else:
                output.append(sortedArr1[i])
                i += 1
                j += 1
        return output       # Return the output array...

nums1 = [1,2,2,1] 
nums2 = [2,2,3]
print(intersection(nums1, nums2))


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))
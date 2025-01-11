"Problem"
#https://leetcode.com/problems/median-of-two-sorted-arrays/description/


"""Explanation  Start by the brute force solution then move to the solution N4(scroll down to the last of the page in chatGPT) 
                and then understand the sol2 adn sol 3"""
#https://chatgpt.com/c/67599990-4f80-8007-ae5a-84ee7d6fd085


#Solution N1

def findMedian_sorted(nums1, nums2):

    ## Merge the arrays into a single sorted array.
    merged = nums1 + nums2

    # Sort the merged array.
    merged.sort()

    n = len(merged)

    # If the total number of elements is odd, return the middle element as the median.
    if n % 2 == 1:
        median= float(merged[n // 2])

    # If the total number of elements is even, calculate the average of the two middle elements as the median.
    else :
        median = float((merged [n // 2 -1]) + merged[n // 2]) / 2


    return median

# Example 1
nums1 = [1, 3]
nums2 = [10,13]
print(findMedian_sorted(nums1, nums2))  # Output: 2.0

# Example 2
nums1 = [1, 2]
nums2 = [3]
print(findMedian_sorted(nums1, nums2))  # Output: 2.5


print("======================================")

#Solution N2:

def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1
        
        # Edge cases: Use -inf and inf for out-of-bound elements
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]
        
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]
        
        # Check if we have found the correct partition
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # Odd total length
            if (m + n) % 2 == 1:
                return float(max(maxLeft1, maxLeft2))
            # Even total length
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
        elif maxLeft1 > minRight2:
            # Move partition1 left
            right = partition1 - 1
        else:
            # Move partition1 right
            left = partition1 + 1

# Example 1
nums1 = [1, 3]
nums2 = [10,13]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

# Example 2
nums1 = [1, 2]
nums2 = [3]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.5




print("======================================")

#Solution N3:

def findMedianSortedArrayss( nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        
        # Ensure nums1 is the smaller array for simplicity
        if n1 > n2:
            return findMedianSortedArrays(nums2, nums1)
        
        n = n1 + n2
        left = (n1 + n2 + 1) // 2 # Calculate the left partition size
        low = 0
        high = n1
        
        while low <= high:
            mid1 = (low + high) // 2 # Calculate mid index for nums1
            mid2 = left - mid1 # Calculate mid index for nums2
            
            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')
            
            # Determine values of l1, l2, r1, and r2
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            
            if l1 <= r2 and l2 <= r1:
                # The partition is correct, we found the median
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # Move towards the left side of nums1
                high = mid1 - 1
            else:
                # Move towards the right side of nums1
                low = mid1 + 1
        
        return 0 # If the code reaches here, the input arrays were not sorted.

# Example 1
nums1 = [1, 3]
nums2 = [10,13]
print(findMedianSortedArrayss(nums1, nums2))  

# Example 2
nums1 = [1, 2]
nums2 = [3]
print(findMedianSortedArrayss(nums1, nums2))  



print("======================================")

#Solution N4:

def ffindMedianSortedArrays(nums1, nums2):
    # Pointers for nums1 and nums2
    i, j = 0, 0
    m, n = len(nums1), len(nums2)
    
    # Total length and median position(s)
    total_len = m + n
    median_idx1 = (total_len - 1) // 2  # Left median position
    median_idx2 = total_len // 2       # Right median position (same as left if odd)
    
    # Variables to store current and previous values
    current, prev = None, None
    
    for count in range(total_len):
        # Update `prev` to the last processed element
        prev = current
        
        # Move the pointers based on comparison
        if i < m and (j >= n or nums1[i] <= nums2[j]):
            current = nums1[i]
            i += 1
        else:
            current = nums2[j]
            j += 1
        
        # Stop if we reach the right median position
        if count == median_idx2:
            # For even total length, return the average of `current` and `prev`
            if total_len % 2 == 0:
                return (current + prev) / 2.0
            # For odd total length, return the middle element
            return float(current)

# Example 1
nums1 = [1, 3]
nums2 = [10,13]
print(ffindMedianSortedArrays(nums1, nums2))  

# Example 2
nums1 = [1, 2]
nums2 = [3]
print(ffindMedianSortedArrays(nums1, nums2))  

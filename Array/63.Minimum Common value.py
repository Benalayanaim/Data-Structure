#Problem 
#https://leetcode.com/problems/minimum-common-value/description/?envType=problem-list-v2&envId=array



"The brute force approach to solving this problem would be to use nested loops to iterate through each number in each array"
"Approach with hashset"
#Solution 1:
def getCommon(nums1, nums2) -> int:
        # Add the elements from nums1 to set1
        set1 = set(nums1)

        # Search for each element of nums2 in set1
        # Return the first common element found
        for num in nums2:
            if num in set1:
                return num

        # Return -1 if there are no common elements
        return -1

nums1 = [1,2,3]
nums2 = [1,4]
print(getCommon(nums1, nums2))

nums1 = [1,2,3,6] 
nums2 = [2,3,4,5]
print(getCommon(nums1, nums2))

"""Explanation :
We found a common element. Since nums2 is sorted in ascending order, the first common element is the minimum common element.
"""




print("=================================================")

#Solution 2:
def getCommon(nums1, nums2) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1.intersection(set2)

        if common:
            return min(common)
        else: 
            return -1
        
nums1 = [1,2,3]
nums2 = [1,4]
print(getCommon(nums1, nums2))

nums1 = [1,2,3,6] 
nums2 = [2,3,4,5]
print(getCommon(nums1, nums2))


print("================================================")

"Approach with Two Pointer"
#Solution 3:
def getCommon(nums1, nums2):
        first = 0
        second = 0

        # Traverse through both arrays with two pointers
        # Increment the pointer with a smaller value at that index
        # Return the first common element found
        while first < len(nums1) and second < len(nums2):
            if nums1[first] < nums2[second]:
                first += 1
            elif nums1[first] > nums2[second]:
                second += 1
            else:
                return nums1[first]

        # Return -1 if there are no common elements
        return -1

nums1 = [1,2,3]
nums2 = [1,4]
print(getCommon(nums1, nums2))

nums1 = [1,2,3,6] 
nums2 = [2,3,4,5]
print(getCommon(nums1, nums2))



print("================================================")
"Appraoch with Binary search "

#Solution 4:
def getCommon(nums1, nums2):
        for num in nums1:
            low = 0
            high = len(nums2)-1
            while low<=high:
                mid = low+(high-low)//2
                if nums2[mid]==num:
                    return num
                elif nums2[mid]<num:
                    low = mid+1
                else:
                    high = mid-1
        return -1

nums1 = [1,2,3]
nums2 = [1,4]
print(getCommon(nums1, nums2))

nums1 = [1,2,3,6] 
nums2 = [2,3,4,5]
print(getCommon(nums1, nums2))


"""Explanation

For each element in nums1, the function performs a binary search on nums2.
When a match is found, the function immediately returns the element.
If no match is found, it continues checking the next element in nums1.
The first common element found is ....
"""

#Explanation for the sol3 and sol 4: https://chatgpt.com/c/67911985-2a38-800f-9a69-fe0140987103



for tomorow :
            










https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/?envType=problem-list-v2&envId=array
https://leetcode.ca/2016-08-22-266-Palindrome-Permutation/

https://leetcode.com/problems/palindromic-substrings/description/

https://leetcode.com/problems/palindrome-number/description/

https://leetcode.com/problems/valid-palindrome/description/








Premieum


https://leetcode.com/problems/group-shifted-strings/description/?envType=problem-list-v2&envId=array
https://leetcode.com/problems/encode-and-decode-strings/description/?envType=problem-list-v2&envId=array

https://leetcode.com/problems/shortest-distance-from-all-buildings/description/?envType=problem-list-v2&envId=array
https://leetcode.com/problems/strobogrammatic-number-iii/description/?envType=problem-list-v2&envId=array

https://leetcode.com/problems/minimum-total-operations/description/?envType=problem-list-v2&envId=array
https://leetcode.com/problems/split-concatenated-strings/description/?envType=problem-list-v2&envId=array

https://leetcode.com/problems/longest-word-with-all-prefixes/description/




hard
https://leetcode.com/problems/minimum-window-substring/description/
https://leetcode.com/problems/first-missing-positive/description/
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/


#Sliding Window
https://leetcode.com/problems/h-index-ii/description/


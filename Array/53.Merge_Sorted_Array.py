"Problem"
#https://leetcode.com/problems/merge-sorted-array/description/?envType=problem-list-v2&envId=array






#Solutio 1:
def merge(nums1, m, nums2, n):
    # Step 1: Take the first m elements from nums1 and all elements from nums2
    temp = nums1[:m] + nums2[:n]
    
    # Step 2: Sort the combined array
    temp.sort()
    
    # Step 3: Copy the sorted array back to nums1
    for i in range(len(temp)):
        nums1[i] = temp[i]

# Example 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1) 

# Example 2
nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)  

# Example 3
nums1 = [1,2,3,4]
m = 2
nums2 = [2,3]
n = 1
merge(nums1, m, nums2, n)
print(nums1) 


print("========================================")

#Solution 2:
def merge(nums1, m, nums2, n):
        nums1[m:] = nums2
        for i in range(len(nums1)):
            for j in range(i,len(nums1)):
                if nums1[i]>=nums1[j]:
                    nums1[i],nums1[j]=nums1[j],nums1[i]

# Example 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1) 

# Example 2
nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)  

# Example 3
nums1 = [1,2,3,4]
m = 2
nums2 = [2,3]
n = 1
merge(nums1, m, nums2, n)
print(nums1) 



print("========================================")

#Solution 3:
def merge(nums1, m, nums2, n):
    nums1[m:] = nums2  # Combine nums2 into nums1
    nums1.sort()       # Use efficient in-built sort function

# Example 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1) 

# Example 2
nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)  

# Example 3
nums1 = [1,2,3,4]
m = 2
nums2 = [2,3]
n = 1
merge(nums1, m, nums2, n)
print(nums1) 


print("========================================")

#Solution 4:
def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()


# Example 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1) 

# Example 2
nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)  

# Example 3
nums1 = [1,2,3,4]
m = 2
nums2 = [2,3]
n = 1
merge(nums1, m, nums2, n)
print(nums1) 


print("==============================================")

#Solution 5:
def merge(nums1, m, nums2, n) : 
        midx = m - 1
        nidx = n - 1 
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1
# Example 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1) 

# Example 2
nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)  

# Example 3
nums1 = [1,2,3,4]
m = 2
nums2 = [2,3]
n = 1
merge(nums1, m, nums2, n)
print(nums1) 




#Explanation : https://chatgpt.com/c/678634b8-e0a4-800f-b811-5598f8dd38c0
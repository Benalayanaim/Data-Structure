#Problem : https://leetcode.com/problems/next-greater-element-i/description/?envType=problem-list-v2&envId=stack








#Solution 1:
def nextGreaterElement(nums1, nums2):
    # Dictionary to store the next greater element for each number in nums2
    next_greater = {}
    stack = []

    # Preprocess nums2 to find the next greater element for each number
    for num in nums2:
        while stack and stack[-1] < num:
            smaller_num = stack.pop()
            next_greater[smaller_num] = num
        stack.append(num)
    
    # For elements still in the stack, there is no next greater element
    while stack:
        next_greater[stack.pop()] = -1

    # Construct the answer for nums1 based on the precomputed dictionary
    return [next_greater[num] for num in nums1]

# Example usage:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(nextGreaterElement(nums1, nums2)) 


print("================================================")
#Solution 2:
def nextGreaterElement(nums1, nums2):
        if not nums2:
            return None

        mapping = {}
        result = []
        stack = []
        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:       # if stack is not empty, then compare it's last element with nums2[i]
                mapping[stack[-1]] = nums2[i]           # if the new element is greater than stack's top element, then add this to dictionary 
                stack.pop()                             # since we found a pair for the top element, remove it.
            stack.append(nums2[i])                      # add the element nums2[i] to the stack because we need to find a number greater than this

        for element in stack:                           # if there are elements in the stack for which we didn't find a greater number, map them to -1
            mapping[element] = -1

        for i in range(len(nums1)):
            result.append(mapping[nums1[i]])
        return result
        

# Example usage:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(nextGreaterElement(nums1, nums2)) 

"""Explanation :
Steps:

We traverse nums2 and start storing elements on the top of stack.
If current number is greater than the top of the stack, then we found a pair. 
    Keep popping from stack till the top of stack is smaller than current number.
After matching pairs are found, push current number on top of stack.
Eventually when there are no more elements in nums2 to traverse, but there are elements in stack, 
    we can justify that next bigger element wasn't found for them. Hence we'll put -1 for the remaining elements in stack."""



print("================================================")
#Solution 2:
def nextGreaterElement(nums1, nums2): 
        ans = []        
        for i in range(len(nums1)):
            current = -1
            idx = len(nums2)
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    idx = j
                if j > idx and nums2[j] > nums1[i]:
                    current = nums2[j]
                    break
            ans.append(current)
        return ans

# Example usage:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(nextGreaterElement(nums1, nums2)) 



print("================================================")
#Solution 2:
def nextGreaterElement(nums1,nums2):
        result = []
        for x in nums1:
            next_greater = -1
            for i in range(len(nums2)):
                if nums2[i] == x:
                    for j in range(i+1, len(nums2)):
                        if nums2[j] > x:
                            next_greater = nums2[j]
                            break
                    break
            result.append(next_greater)
        
        return result



# Example usage:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(nextGreaterElement(nums1, nums2)) 




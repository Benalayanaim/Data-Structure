#https://leetcode.com/problems/product-of-array-except-self/description/



#Solution 1:
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n  # Initialize the answer array with 1s

    # Step 1: Compute left product for each index
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    # Step 2: Compute right product and combine with left product
    right_product = 1
    for i in range(n - 1, -1, -1):  # Traverse from right to left
        answer[i] *= right_product
        right_product *= nums[i]

    return answer

# Example usage
nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]

print(product_except_self(nums1))  # Output: [24, 12, 8, 6]
print(product_except_self(nums2))  # Output: [0, 0, 9, 0, 0]


print("============================")



#Solution 2:

def Product_fo_array(nums):
    n = len(nums)
    result = []
    for i in range(n):
        pro = 1
        for j in range(n):
            if(i==j):
                continue

            pro *=nums[j]

        result.append(pro)
    return result

nums1 = [1,2,3,4]
nums = [-1,1,0,-3,3]

print(Product_fo_array(nums))
print(Product_fo_array(nums1))


#Explnation
""" Brute Force
So, the first and formost, the simplest method that comes to mind is, I can loop through the complete array 
using a pointer, say j, for every index i, and multiply all the elements at index j except when i == j. 
This would ensure that I skip the element at index i from being multiplied."""


print("==============================")

#Solution 3

def product_except_self(nums):
    n = len(nums)
    
    # Step 1: Create prefix and suffix arrays
    prefix = [1] * n
    suffix = [1] * n
    result = [0] * n
    
    # Step 2: Fill the prefix array
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    
    # Step 3: Fill the suffix array
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    
    # Step 4: Combine prefix and suffix to compute the result
    for i in range(n):
        result[i] = prefix[i] * suffix[i]
    
    return result

nums1 = [1,2,3,4]
nums = [-1,1,0,-3,3]


print(product_except_self(nums))
print(product_except_self(nums1))


"Explanation "
#https://chatgpt.com/c/67505686-b930-8007-9737-116ecc4ff97a
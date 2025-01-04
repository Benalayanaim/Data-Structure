
#https://leetcode.com/problems/maximum-product-subarray/description/




#Solution 1:
def max_product_subarray_brute_force(nums):
    if not nums:
        return 0

    n = len(nums)
    max_product = float('-inf')  # Initialize to the smallest possible value

    for i in range(n):          # Outer loop: start of the subarray
        product = 1             # Reset product for each new subarray
        for j in range(i, n):   # Inner loop: end of the subarray
            product *= nums[j]  # Multiply elements in the subarray
            max_product = max(max_product, product)  # Update the maximum product

    return max_product



nums1 = [2,3,-2,4]

nums2 = [-2,0,-1]

print(max_product_subarray_brute_force(nums1))
print(max_product_subarray_brute_force(nums2))










print("=============strugle===============")

#Solution 2:
def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = min_product = result = nums[0]

    for num in nums[1:]:
        if num < 0:
            # Swap max_product and min_product when num is negative
            max_product, min_product = min_product, max_product

        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        result = max(result, max_product)

    return result
nums1 = [2,3,-2,4]

nums2 = [-2,0,-1]

print(max_product_subarray(nums1))
print(max_product_subarray(nums2))



print("=============strugle===============")

#Solution 3:


def maxxProduct(nums):
    prefix = 1
    suffix = 1

    n = len(nums)
    ans = -float('inf')

    for i in range(len(nums)):
        if prefix == 0 :
            prefix = 1
        if suffix == 0:
            suffix = 1
        prefix = prefix*nums[i]
        suffix = suffix*nums[n-i-1]

        ans = max(prefix, ans, suffix)
    
    return ans

nums1 = [2,3,-2,4]

nums2 = [-2,0,-1]




print(maxxProduct(nums1))
print(maxxProduct(nums2))




"""Approach
Calculate the prefix sum
Calculate the suffix sum
If any one of them is zero make it again 1 as it will not be useful is prefix or suffix is zero.
Return max(ans,suffix,prefix)"""




#Explanation : https://chatgpt.com/c/675235bb-eaa0-8007-92ff-0b669349c71b
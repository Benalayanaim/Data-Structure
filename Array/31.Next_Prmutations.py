"Problem"
#https://leetcode.com/problems/next-permutation/description/




#Solution N:1

def nextPermutation(nums):
    # Step 1: Find the pivot point
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:  # There is a valid pivot
        # Step 2: Find the successor
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap pivot and successor
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse the suffix
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums

nums = [8, 3, 5, 8, 7]

print(nextPermutation(nums))


print("=============================================")

#Solution 2:
def nextPermutation1(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # To find next permutations, we'll start from the end
        i = j = len(nums)-1
        # First we'll find the first non-increasing element starting from the end
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # After completion of the first loop, there will be two cases
        # 1. Our i becomes zero (This will happen if the given array is sorted decreasingly). In this case, we'll simply reverse the sequence and will return 
        if i == 0:
            nums.reverse()
            return 
        # 2. If it's not zero then we'll find the first number grater then nums[i-1] starting from end
        while nums[j] <= nums[i-1]:
            j -= 1
        # Now out pointer is pointing at two different positions
        # i. first non-assending number from end
        # j. first number greater than nums[i-1]
        
        # We'll swap these two numbers
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # We'll reverse a sequence strating from i to end
        nums[i:]= nums[len(nums)-1:i-1:-1]

nums = [8, 3, 5, 8, 7]
nextPermutation1(nums)
print(nums)


print("=============================================")

#Solution 3:
def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)

    for i in range(n - 1, 0, -1):
        curr = nums[i]
        next = nums[i - 1]
        if next < curr:
            nums[i:] = nums[n - 1 : i - 1 : -1]  # Reverse the suffix
            # search insert point
            k = i
            while next >= nums[k]:
                k += 1
            # swap with first bigger from next
            nums[i - 1] = nums[k]
            nums[k] = next
            return
nums = [8, 3, 5, 8, 7]
nextPermutation1(nums)
print(nums)



#Explanation : https://chatgpt.com/c/676d2feb-d670-8007-823f-55b550277845

#Problem: https://leetcode.com/problems/sort-colors/description/?envType=problem-list-v2&envId=array




#Solution 1:
def sort_colors(nums):
    """
    Sorts an array of integers representing colors (0 - red, 1 - white, 2 - blue) in-place.
    """
    # Count the occurrences of 0s, 1s, and 2s
    count = [0, 0, 0]
    for num in nums:
        count[num] += 1

    # Fill the original array with the sorted colors
    index = 0
    for i in range(3):
        while count[i] > 0:
            nums[index] = i
            index += 1
            count[i] -= 1

# Example usage:
nums = [2, 0, 2, 1, 1, 0]
print("Original Array:", nums)
sort_colors(nums)
print("Sorted Array:", nums)

nums = [2, 0, 1]
print("\nOriginal Array:", nums)
sort_colors(nums)
print("Sorted Array:", nums)



print("====================================================")


#Soluiton 2:
def sort_colors(nums):
        n=len(nums)
        for i in range(n-1,-1,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    temp=nums[j+1]
                    nums[j+1]=nums[j]
                    nums[j]=temp
        return nums


# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sort_colors(nums)
print(nums)  

print("====================================================")


#Soluiton 3:
def sort_colors(nums):
    red = 0
    white = 0
    blue = len(nums) - 1
    
    while white <= blue:
        if nums[white] == 0:
            nums[white], nums[red] = nums[red], nums[white]
            red += 1
            white += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1

print("====================================================")

#Solution 4:
def sortColors(nums):
    # Step 1: Count the number of 0s, 1s, and 2s
    count0 = nums.count(0)
    count1 = nums.count(1)
    count2 = nums.count(2)
    
    # Step 2: Overwrite the array with 0s, 1s, and 2s in order
    nums[:count0] = [0] * count0
    nums[count0:count0 + count1] = [1] * count1
    nums[count0 + count1:] = [2] * count2

# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  


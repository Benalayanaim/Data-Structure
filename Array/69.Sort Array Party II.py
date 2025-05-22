#Problem : https://leetcode.com/problems/sort-array-by-parity-ii/description/?envType=problem-list-v2&envId=array




#Solution 1:

def sortArrayByParityII(nums):
    odd = []
    even = []
    result = []

    for num in nums:
        if num % 2 == 0: 
            even.append(num)
        else:
            odd.append(num)
    #we loop just to the half because, we append from the array even and odd and these two is the half of the array nums
    for i in range(len(nums) // 2):
   #for i in range(len(even)):
        result.append(even[i])
        result.append(odd[i])

    return result

nums = [1,2,3,4]
print(sortArrayByParityII(nums))


print("=================================================")
#Solution 2:

def sortArrayByParityII(nums):
    arr=[0]*len(nums)
    even=0
    odd=1

    for i in range(len(nums)):
        if nums[i]%2==0:
            arr[even]=nums[i]
            even+=2
        else:
            arr[odd]=nums[i]
            odd+=2

    return arr


nums = [1,2,3,4]
print(sortArrayByParityII(nums))

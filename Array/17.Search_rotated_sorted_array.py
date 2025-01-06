#https://leetcode.com/problems/search-in-rotated-sorted-array/description/



#Solution :
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    
    return -1

print(search([15, 17, 19, 1, 2, 5, 7, 10, 12],10))


print("=====================")

#Solution :
def search_rotated_sorted_array(nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1


print(search_rotated_sorted_array([15, 17, 19, 1, 2, 5, 7, 10, 12],10))



#Explanation for the code :
#https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/5378208/video-find-a-sorted-part-in-ascending-order/

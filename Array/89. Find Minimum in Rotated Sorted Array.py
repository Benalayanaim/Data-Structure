#Problem
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=array









#Solution 1:
def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # If mid element is greater than the right element, the min must be in the right half.
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Otherwise, the min is in the left half (including mid).
            right = mid
            
    # When the loop ends, left == right, pointing to the minimum element.
    return nums[left]

# Example test cases
print(findMin([3,4,5,1,2]))     
print(findMin([4,5,6,7,0,1,2])) 
print(findMin([11,13,15,17]))   



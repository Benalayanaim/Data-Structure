"Problem"
#https://leetcode.com/problems/find-peak-element/description/




#For the 4 solution

"Start by the explanation in the link firstly"
#Explnation : https://leetcode.com/problems/find-peak-element/solutions/788474/general-binary-search-thought-process-4-templates/

"then watch teh videos"
#https://www.youtube.com/watch?v=GU7DpgHINWQ&t=67s







print("====================")

#Solution : 5
def findPeakElement1(nums) -> int:
        nums = [-float('inf')] + nums + [-float('inf')]

        mid = (0 + len(nums) - 1) // 2

        while 0 < mid < len(nums) - 1:
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid - 1
            elif nums[mid - 1] > nums[mid + 1]: 
                mid -= 1
            else:
                mid += 1

nums = [3,2,1]
nums1 = [1,2,1,3,5,6,4]
nums2 = [1,2,6,3,5,4,4]
print(findPeakElement1(nums))
print(findPeakElement1(nums1))
print(findPeakElement1(nums2))

print("====================")


#Solution : 6
def findPeakElement2(nums):
    # Enumerate to keep track of indices
    peak_index = max(range(len(nums)), key=lambda i: nums[i])
    return peak_index
nums = [3,2,1]
nums1 = [1,2,1,3,5,6,4]
nums2 = [1,2,6,3,5,4,4]
print(findPeakElement2(nums))
print(findPeakElement2(nums1))
print(findPeakElement2(nums2))

print("====================")



#Solution : 7
def findPeakElement(nums):
    return nums.index(max(nums))
nums = [3,2,1]
nums1 = [1,2,1,3,5,6,4]
nums2 = [1,2,6,3,5,4,4]
print(findPeakElement(nums))
print(findPeakElement(nums1))
print(findPeakElement(nums2))

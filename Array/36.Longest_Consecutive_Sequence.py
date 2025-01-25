"Problem"
#https://leetcode.com/problems/longest-consecutive-sequence/description/





#Solution 1

def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Check if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count the length of the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Example usage
nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [10,5,9,7,8]
print(longestConsecutive(nums1))  
print(longestConsecutive(nums2))  


print("=================================")

#Solution 2 :
def longestConsecutive(nums): 
    if nums == []:
        return 0

    if len(nums) == 1:
        return 1

    m = {}
    
    for num in nums:
        m[num] = num

    longest_streak = 0

    for num in m.keys():
        if num - 1 not in m.keys():
            streak = 0  # Start from 0

            while num + streak in m.keys():
                streak += 1

            longest_streak = max(longest_streak, streak)

    return longest_streak


# Example usage
nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [10,5,9,7,8]
print(longestConsecutive(nums1))  
print(longestConsecutive(nums2))  


print("=================================")

#Solution 3 :

def longestConsecutive(nums):
    if not nums:
        return 0
    
    nums.sort()

    maxLength = 1
    currentLength = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if nums[i] == nums[i - 1] + 1:
                currentLength += 1
            else:
                currentLength = 1

            maxLength = max(maxLength, currentLength)

    return maxLength


# Example usage
nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [10,5,9,7,8]
print(longestConsecutive(nums1))  
print(longestConsecutive(nums2))  


print("=================================")

#Solution 4 :

def longestConsecutive(nums) :
        
        if len(nums) == 0:
            return 0
        
        clean = sorted(set(nums))
        
        last = None
        count = 1
        max_len = 0

        for x in clean:
            if x - 1 == last:
                count += 1
            else:
                
                if count > max_len:
                    max_len = count
                count = 1 
            last = x

        if count > max_len:
            max_len = count

        return max_len

# Example usage
nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [10,5,9,7,8]
print(longestConsecutive(nums1))  
print(longestConsecutive(nums2))  





#https://leetcode.com/problems/two-sum/description/

def two_sum(nums, target):
    n = len(nums)
    for i in range (n - 1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]
    
    return[]

nums = [3,3,3]
target = 6

print(two_sum(nums, target))


#Another solution here 
#https://leetcode.com/problems/two-sum/solutions/3619262/3-method-s-c-java-python-beginner-friendly/


def twosum2(numss, t):

    numMap = {}
    n = len(nums)

    for i in range(n):

            complement = t - numss[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[numss[i]] = i

    return []  # No solution found
numss = [3,3,3]
t = 6

print(two_sum(numss, t))




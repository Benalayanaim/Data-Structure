#Problem 
#https://leetcode.com/problems/shuffle-the-array/?envType=problem-list-v2&envId=array




#Solution 1:

def shuffle(nums, n):
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            res += [i,j]
        return res
#OR     return list(chain(*zip(nums[:n],nums[n:])))

nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums, n))

nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums, n))

nums = [1,1,2,2]
n = 2
print(shuffle(nums, n))

"""Explaination for the solution and 
what is the * """
#Explanation https://chat.deepseek.com/a/chat/s/d55eec95-c960-402a-8f55-e995b1c8b153

print("=======================================================")

#Solution 1:

def shuffle(nums, n):
        lst=[]

        for i in range(n):
            lst+=[nums[i]]
            lst+=[nums[i+n]]

        return lst
nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums, n))

nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums, n))

nums = [1,1,2,2]
n = 2
print(shuffle(nums, n))


print("=======================================================")

#Solution 1:

def shuffle(nums, n):
        ans = [] 
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums, n))

nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums, n))

nums = [1,1,2,2]
n = 2
print(shuffle(nums, n))



print("=======================================================")

#Solution 1:

def shuffle(nums, n):
        j = n
        results = []

        for i in range(len(nums)-n):
            results.append(nums[i])
            results.append(nums[j])
            j += 1
        return results
nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums, n))

nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums, n))

nums = [1,1,2,2]
n = 2
print(shuffle(nums, n))



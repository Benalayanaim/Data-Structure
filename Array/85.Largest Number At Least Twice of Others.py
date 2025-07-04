#Problem
#https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/?envType=problem-list-v2&envId=array



#Solution 1:

def dominantIndex(nums):
    maxi=max(nums)
    index=nums.index(maxi)
    nums.remove(maxi)
    maxi2=max(nums)
    if maxi>=2*maxi2:
        return index
    else:
        return -1

nums = [3,6,1,0]
print(dominantIndex(nums))

nums = [1,2,3,4]
print(dominantIndex(nums))





print("=================================================")

#Solution 2:

from pickle import deepcopy
def dominantIndex(nums):
        a=max(nums)
        b=deepcopy(nums) 
        b.remove(a)
        
        for num in b:
            #keep iterating through all num 
            if a >= num*2:
                continue
            #if there is oe num > a, return -1
            else : 
                return -1
            
        #after iterate through all num and  the condtion(continue) True return the index
        return nums.index(a)
      

nums = [3,6,1,0]
print(dominantIndex(nums))

nums = [1,2,3,4]
print(dominantIndex(nums))

""" menejmouch naamlou heke  khater heke bech ya3mil iteration whadaa barkaa w fii cas kima example deux expected out put hiee -1, but bii ktibaa hedhiee bech yrodnaa l'index elii hiee ghalettt
for num in b:
            if a >= num*2:
                return nums.index(a)
        return -1"""





print("=================================================")

#Solution 2:

def dominantIndex(nums):  
    m = max(nums)
    if all(m >= 2*x for x in nums if x != m):
        return nums.index(m)
    return -1
      
      
nums = [3,6,1,0]
print(dominantIndex(nums))

nums = [1,2,3,4]
print(dominantIndex(nums))

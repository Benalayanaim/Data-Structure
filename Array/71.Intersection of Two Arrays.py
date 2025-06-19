#Problem
#https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=problem-list-v2&envId=array




#Solution 1:
def intersection(nums1, nums2):
        res = set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    res.add(i)
                    break


        return list(res)

nums1 = [1,2,2,1] 
nums2 = [2,2,3]
print(intersection(nums1, nums2))


print("=================================================")

#Solution 2:
def intersection(nums1, nums2):
        intersection = []
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in intersection:
                intersection.append(nums1[i])
        return intersection

nums1 = [1,2,2,1] 
nums2 = [2,2,3]
print(intersection(nums1, nums2))

print("=================================================")


#Solution 3:
def intersection(nums1, nums2):
        seen = set()
        res = []
        
        for num in nums1:
            seen.add(num)
        
        for num in nums2:
            if num in seen and num not in res:
                res.append(num)
        
        return res

nums1 = [1,2,2,1] 
nums2 = [2,2,3]
print(intersection(nums1, nums2))

print("=================================================")


#Solution 4:
def intersection(nums1, nums2):
        nums1.sort()
        nums2.sort()
        i,j=0,0
        a=[]
        while i!=len(nums1) and j!=len(nums2):
            if nums1[i]==nums2[j]:
                a.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        return list(set(a))

nums1 = [1,2,2,1] 
nums2 = [2,2,3]
print(intersection(nums1, nums2))

print("=================================================")

#Solution 5:
def intersection(nums1, nums2):
        
        # Convert both lists to set to remove duplicates and get unique elements 
        set1 = set(nums1)
        set2 = set(nums2)
        
        
        # Find the intersection of the two sets
        result = set1 & set2 
        
        
        
        
        # Convert the result to a list and return it
        return list(result)

nums1 = [1,2,2,1] 
nums2 = [2,2,3]
print(intersection(nums1, nums2))


print("=================================================")

#Solution 5:
def intersection(nums1, nums2):
        
        # Convert both lists to set to remove duplicates and get unique elements 
        set1 = set(nums1)
        set2 = set(nums2)
        
        
        # Find the intersection of the two sets
        result = set1.intersection(set2) 
        
        
        
        
        # Convert the result to a list and return it
        return list(result)

nums1 = [1,2,2,1] 
nums2 = [2,2,3]
print(intersection(nums1, nums2))






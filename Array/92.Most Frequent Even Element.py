#Problem
#https://leetcode.com/problems/most-frequent-even-element/description/




#Solution 1:
def mostFrequentEven(nums) -> int:
        hm = {}
        for num in nums:
            if (num % 2 == 0):
                if (num in hm):
                    hm[num] += 1
                else:
                    hm[num] = 1
        best = 0
        best_key = -1

        for key, val in hm.items():
            if val > best:
                best = val
                best_key = key
            elif val == best:
                best_key = min(key, best_key)
        return best_key

nums = [0,1,2,2,4,4,1]
print(mostFrequentEven(nums))

nums = [4,4,4,9,2,4]
print(mostFrequentEven(nums))

nums = [29,47,21,41,13,37,25,7]
print(mostFrequentEven(nums))


print("============================================================")

#Solution 2:
def mostFrequentEven(nums) -> int:
        c={}
        for i in nums:
            if i%2==0:
                c[i]=c.get(i,0)+1
        if len(c)==0:
            return -1
        m=[]
        k=(max(c.values()))
        for i,j in c.items():
            if j==k:
                m.append(i)
        m.sort()
        return (m[0])

print("============================================================")

#Solution 2:
def mostFrequentEven(nums) -> int:
        resultt= []
        max = 0
        for num in set(nums):  
            if num % 2 == 0:
                count_num = nums.count(num)  
                if count_num > max:
                    resultt = [num]  
                    max = count_num
                elif count_num == max:
                    resultt.append(num)
        if resultt:
            return min(resultt) 

        return -1

nums = [0,1,2,2,4,4,1]
print(mostFrequentEven(nums))

nums = [4,4,4,9,2,4]
print(mostFrequentEven(nums))

nums = [29,47,21,41,13,37,25,7]
print(mostFrequentEven(nums))
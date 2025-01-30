"Problem"
#https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/



#Solution N1:
def countSmaller(nums):
    # Map numbers to their rank
    sorted_nums = sorted(set(nums))
    rank_map = {num: rank + 1 for rank, num in enumerate(sorted_nums)}
    
    # Binary Indexed Tree
    def update(index, value, bit, size):
        while index <= size:
            bit[index] += value
            index += index & -index
    
    def query(index, bit):
        total = 0
        while index > 0:
            total += bit[index]
            index -= index & -index
        return total
    
    # Initialize variables
    n = len(nums)
    bit = [0] * (len(sorted_nums) + 1)
    counts = [0] * n
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        rank = rank_map[nums[i]]
        counts[i] = query(rank - 1, bit)
        update(rank, 1, bit, len(sorted_nums))
    
    return counts

# Test cases
print(countSmaller([5, 2, 6, 1])) 
print(countSmaller([-1]))         
print(countSmaller([-1, -1]))    




print("=====================================")


#Solution N2:

def countSmaller1(nums): 
        nums = nums[::-1]
        min_v = min(nums) if nums else 0
        
        import collections
        record = collections.defaultdict(int)
        
        res = []
        for n in nums:
            cnt = 0
            for target in range(min_v,n):
                if target in record:
                    cnt += record[target]
            res.append(cnt)
            record[n]+=1
        return res[::-1]

# Test cases
print(countSmaller1([5, 2, 6, 1]))  
print(countSmaller1([-1]))         
print(countSmaller1([-1, -1]))     

"""Updated Solution with record = {}:
def countSmaller(nums): 
    nums = nums[::-1]
    min_v = min(nums) if nums else 0

    record = {}  # Regular dictionary

    res = []
    for n in nums:
        cnt = 0
        for target in range(min_v, n):
            if target in record:
                cnt += record[target]
        res.append(cnt)
        record[n] = record.get(n, 0) + 1  # Ensure safe key update
    return res[::-1]
"""


print("=====================================")

#Solution N3:
def countSmaller2(nums): 
        nums = nums[::-1]
        nums = [(n,i) for i,n in enumerate(nums)]
        res = [0]*len(nums)
        
        def mergesort(l,r):
            if l == r:
                return 
            mid = (l+r)//2
            mergesort(l,mid)
            mergesort(mid+1,r)
            
            i = l
            # O(n)
            for j in range(mid+1,r+1):
                while i < mid+1 and nums[i][0] < nums[j][0]:
                    i += 1
                res[nums[j][1]] += i-l
       
            nums[l:r+1] = sorted(nums[l:r+1])
            
        mergesort(0,len(nums)-1) if nums else None
        return res[::-1]

# Test cases
print(countSmaller2([5, 2, 6, 1])) 
print(countSmaller2([-1]))         
print(countSmaller2([-1, -1]))     



print("=====================================")

#Solution N4:

def countSmaller4(nums): 
        """
        count smaller items using binary index tree, start from the right side
        """
        offset = min(nums) - 1
        N = max(nums) - offset
        
        buf = [0] * (N + 1)
        res = []
        for n in nums[::-1]:
            index = n - offset - 1
            count = 0
            
            while index > 0:
                count += buf[index]
                index -= (index & -index)
            res.append(count)
            
            index = n - offset
            while index < N:
                buf[index] += 1
                index += (index & -index)
                
        return res[::-1]

# Test cases
print(countSmaller4([5, 2, 6, 1]))  
print(countSmaller4([-1]))         
print(countSmaller4([-1, -1]))     



#Explanation : https://chatgpt.com/c/6780f169-704c-800f-a0b0-c703d9c21afc

"Python Bitwise Operators"
#Resource : https://www.geeksforgeeks.org/python-bitwise-operators/
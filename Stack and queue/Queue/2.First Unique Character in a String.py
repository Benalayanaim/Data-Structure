#Problem : https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue




"Hashmap"
#Solution 1:

from collections import Counter
def firstUniqChar(s: str) -> int:
        
        # build hash map: character and how often it appears
        count = Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx   #the first charcter found it willl return  
        return -1

s = "naim"
print(firstUniqChar(s))

s = "CCTCCA"
print(firstUniqChar(s))

s = "aabb"
print(firstUniqChar(s))

print("================================================")

#Solution 2:
def firstUniqChar( s: str) -> int:
        st=list(s)
        fre=Counter(list(s))
        for i,j in fre.items():
            if j==1:
                return st.index(i)
        return -1 

s = "naim"
print(firstUniqChar(s))

s = "CCTCCA"
print(firstUniqChar(s))

s = "aabb"
print(firstUniqChar(s))



print("================================================")

#Solution 3:
def Solution2(s: str) -> int:
        mp = {}

        for char in s:
            mp[char] = mp.get(char, 0) + 1

        for i in range(len(s)):
            if mp[s[i]] == 1:
                return i

        return -1

s = "naim"
print(Solution2(s))

s = "CCTCCA"
print(Solution2(s))

s = "aabb"
print(Solution2(s))

#Explanation : for thhis solution solution mi chat mte3iii
#https://chatgpt.com/c/67978eea-5ae4-800f-9fdb-608371c82f48


print("================================================")

#Solution 4:
def solution1(s: str) -> int:
        # cntr = Counter(s)
        cntr = {}
        for c in s:
            if c not in cntr:
                cntr[c] = 0
            cntr[c] += 1

        for i in range(len(s)):
            if cntr[s[i]] == 1:
                return i
        return -1


s = "naim"
print(solution1(s))

s = "CCTCCA"
print(solution1(s))

s = "aabb"
print(solution1(s))

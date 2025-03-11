#Problem : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/?envType=problem-list-v2&envId=stack




#Solution 1
def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
        #if(len(stack)>0 and stack[-1] == char:
            stack.pop()  
        
        else:
            stack.append(char)  
    return ''.join(stack)  # Combine characters to form the resulting string

# Example 1
s1 = "abbaca"
print( remove_adjacent_duplicates(s1))  

# Example 2
s2 = "azxxzy"
print( remove_adjacent_duplicates(s2))  



print("=======================================")

#Solution 2:
def removeDuplicates(s):
    if len(s) < 2:
        return s

    new_s = [s[0]]
    for i in range(1, len(s)):
        if new_s and s[i] == new_s[-1]:
            new_s.pop()
        else:
            new_s.append(s[i])  # Use append instead of += for better performance

    return ''.join(new_s)
# Example 1
s1 = "abbaca"
print( remove_adjacent_duplicates(s1))  

# Example 2
s2 = "azxxzy"
print( remove_adjacent_duplicates(s2))  




print("=======================================")

#Solution 3:
def removeDuplicates( s: str) -> str:
        s = list(s)
        st = []
        for i in range(len(s)):
            if st and s[i] == st[-1]:
                st.pop()

            else:
                st.append(s[i])
        return ''.join(st)

# Example 1
s1 = "abbaca"
print(remove_adjacent_duplicates(s1))  

# Example 2
s2 = "azxxzy"
print(remove_adjacent_duplicates(s2))  





print("=======================================")

#Solution 4:
def removeDuplicates( s: str) : 
        res=list(s)
        slow=fast=0
        while fast<len(res):
            res[slow]=res[fast]
            if slow>0 and res[slow]==res[slow-1]:
                slow -=1
            else:
                slow +=1
            fast +=1
        return ''.join(res[0:slow])


# Example 1
s1 = "abbaca"
print(remove_adjacent_duplicates(s1))  

# Example 2
s2 = "azxxzy"
print(remove_adjacent_duplicates(s2))  




#Explanation : https://chatgpt.com/c/678a3a7a-50c8-800f-be20-b586bc22d147
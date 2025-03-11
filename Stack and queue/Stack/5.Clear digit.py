#Problem : https://leetcode.com/problems/clear-digits/description/?envType=problem-list-v2&envId=stack



#Solution 1:
def clearDigits(s: str) -> str:
        st = []
        for ch in s:
            if '0' <= ch <= '9' and st:
                st.pop()
            else:
                st.append(ch)
        
        s = "".join(st)
        return s


s = "a4b3c"
s1 = "abc34"


print(clearDigits(s))
print(clearDigits(s1))

print("=======================================")

#Solution 2:
def clearDigits( s: str) -> str:
    stack = []
    for elem in s:
        if elem.isdigit():
            stack.pop()
        else:
            stack.append(elem)
    return ''.join(stack)

s = "a4b3c"
s1 = "abc34"

print(clearDigits(s))
print(clearDigits(s1))



print("=======================================")


#Solution 3:
from collections import deque
def clearDigits(s: str) -> str:

    stack = deque()

    for ch in s:
        if ch.islower(): 
            stack.append(ch)

        else: stack.pop()

    return ''.join(stack)


s = "a4b3c"
s1 = "abc34"

print(clearDigits(s))
print(clearDigits(s1))





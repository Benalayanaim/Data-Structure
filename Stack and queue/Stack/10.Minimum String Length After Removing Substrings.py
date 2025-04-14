#Problem : https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/?envType=problem-list-v2&envId=stack






#solution 1:
def minLength(s: str) -> int:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if c == "B" and stack[-1] == "A":
                stack.pop()
            elif c == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(c)
        return len(stack)

s = "ABFCACDB"
s1 = "ACBBD"

print(minLength(s))
print(minLength(s1))

print("==============================================")

#solution 2:
def minLength(s: str) -> int:
    stack = []
    for c in s:
      if stack and ((c == "B" and stack[-1]=="A") or (c=="D" and stack[-1]=="C")):
          stack.pop()
      else:
        stack.append(c)
    return len(stack)

s = "ABFCACDB"
s1 = "ACBBD"

print(minLength(s))
print(minLength(s1))


print("==============================================")

#solution 3:
def minLength(s: str) -> int:
    while 'AB' in s or 'CD' in s:
            print('AB' in s)
            if 'AB' in s:
                print('here')
                ab_pos = s.index('AB')
                s = s[:ab_pos]+s[ab_pos+2:]
                print('after removing AB :', s)

            if 'CD' in s:
                ab_pos = s.index('CD')
                s = s[:ab_pos]+s[ab_pos+2:]
                print('after removing CD :', s)
    return(len(s))

s = "ABFCACDB"
s1 = "ACBBD"

print(minLength(s))
print(minLength(s1))

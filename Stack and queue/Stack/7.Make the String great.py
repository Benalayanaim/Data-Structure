#Problem : https://leetcode.com/problems/make-the-string-great/description/?envType=problem-list-v2&envId=stack



#Solution 1
def makeGood(s: str) -> str:
    stack = []
    for char in s:
        # Check if the stack is not empty and the last character in the stack and current character form a "bad" pair
        if stack and abs(ord(stack[-1]) - ord(char)) == 32:
            stack.pop()  # Remove the bad pair
        else:
            stack.append(char)  # Add the current character to the stack
    return ''.join(stack)


print(makeGood("leEeetcode"))  
print(makeGood("abBAcC"))      
print(makeGood("s"))           



print("========================================")

#Solution 2:
def makeGood(s):
        output=[]
        for i in s:
            if output and output[-1].lower()==i.lower() and ord(output[-1])!=ord(i):
                output.pop()
            else:
                output.append(i)
        return "".join(output)


print(makeGood("leEeetcode"))  
print(makeGood("abBAcC"))      
print(makeGood("s"))           



print("========================================")

#Solution 3:
def makeGood(s) : 
        if len(s) == 1:
            return s

        length = len(s)
        prev_length= -1

        while length != prev_length and length > 1:
            prev_length = length
            lp= 0
            while lp < (length - 1):
                if abs(ord(s[lp]) - ord(s[lp + 1])) == 32:
                    if lp == 0:
                        s = s[lp + 2:]
                    else:
                        s = s[0:lp] + s[lp + 2: length]
                    length = length - 2
                    break
                lp += 1

        return s

print(makeGood("leEeetcode"))  
print(makeGood("abBAcC"))      
print(makeGood("s"))           


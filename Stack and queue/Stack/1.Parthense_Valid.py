#Problem : https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=stack

"""Description of the problem:
The problem requires us to determine if the given string of brackets is valid or not. We can use a stack data structure 
to keep track of opening brackets encountered and check if they match with the corresponding closing brackets."""



#Solution 1:
def isValid(s: str) -> bool:
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    # Iterate through each character in the string
    for char in s:
        if char in bracket_map:
            # Pop the top of the stack if it exists; otherwise use a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the current closing bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # Push opening brackets onto the stack
            stack.append(char)

    # If the stack is empty, the string is valid
    return not stack


print(isValid("()"))        
print(isValid("()[]{}"))    
print(isValid("(]"))        
print(isValid("([])"))      




print("================================================")

#Solution 2:
def isValid(s):
        stack = [] # create an empty stack to store opening brackets
        for c in s: # loop through each character in the string
            if c in '([{': # if the character is an opening bracket
                stack.append(c) # push it onto the stack
            else: # if the character is a closing bracket
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False # the string is not valid, so return false
                stack.pop() # otherwise, pop the opening bracket from the stack
        return not stack # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
                         # so the string is valid, otherwise, there are unmatched opening brackets, so return falseprint(isValid("()"))  

print(isValid("()"))                  
print(isValid("()[]{}"))    
print(isValid("(]"))        
print(isValid("([])"))      


"""Explanation :
Here is the step-by-step approach of the algorithm:

1/Initialize an empty stack.

2/Traverse the input string character by character.

3/If the current character is an opening bracket (i.e., '(', '{', '['), push it onto the stack.

4/If the current character is a closing bracket (i.e., ')', '}', ']'), check if the stack is empty. If it is empty, 
return false, because the closing bracket does not have a corresponding opening bracket. Otherwise, 
pop the top element from the stack and check if it matches the current closing bracket. 
If it does not match, return false, because the brackets are not valid.

5/After traversing the entire input string, if the stack is empty, return true, 
because all opening brackets have been matched with their corresponding closing brackets. 
Otherwise, return false, because some opening brackets have not been matched with their corresponding closing brackets."""




print("================================================")

#Solution 3:

def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets

        for char in s:
            if char in bracket_pairs.values():  # If it's an opening bracket
                stack.append(char)
            elif char in bracket_pairs.keys():  # If it's a closing bracket
                if not stack or stack[-1] != bracket_pairs[char]:  # Check if stack is empty or mismatched
                    return False
                stack.pop()  # Pop the matching opening bracket
            else:  # Invalid character
                return False

        return not stack  # If stack is empty, the string is valid


print(isValid("()"))                  
print(isValid("()[]{}"))    
print(isValid("(]"))        
print(isValid("([])"))      



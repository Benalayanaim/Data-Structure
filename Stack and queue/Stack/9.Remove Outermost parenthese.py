#Problem : https://leetcode.com/problems/remove-outermost-parentheses/description/?envType=problem-list-v2&envId=stack
"Watch just the first 4 minute "
#Video to undestand the problem : https://www.youtube.com/watch?v=I0osO1BqiGw







#solution 1:
def removeOuterParentheses(s: str) -> str:
    """
    Remove outermost parentheses from each primitive string in the primitive decomposition of s.
    
    Args:
        s (str): A valid parentheses string.
    
    Returns:
        str: The resulting string after removing outermost parentheses.
    """
    result = ""
    balance = 0
    temp = ""
    
    for char in s:
        temp += char
        
        # If we encounter an opening parenthesis, decrement the balance counter
        if char == "(":
            balance += 1
        # If we encounter a closing parenthesis, increment the balance counter
        elif char == ")":
            balance -= 1
        
        # If the balance counter is zero, we have found a primitive string
        if balance == 0:
            # Remove the outermost parentheses from the primitive string and add it to the result
            result += temp[1:-1]
            # Reset the temporary string and balance counter
            temp = ""
    
    return result

# Example usage
print(removeOuterParentheses("(()())(())")) 
print(removeOuterParentheses("(()())(())(()(()))"))  
print(removeOuterParentheses("()()"))  


"""Explanation :
### Algorithm

The algorithm to solve this problem involves the following steps:

1. **Initialize variables**: Initialize an empty result string and a counter to keep track of the balance of parentheses.
2. **Iterate over the input string**: Iterate over each character in the input string `s`.
3. **Update the counter**: If the character is an opening parenthesis `(`, decrement the counter. 
    If the character is a closing parenthesis `)`, increment the counter.

4. **Check for primitive strings**: If the counter is zero, it means we have found a primitive string. 
    Remove the outermost parentheses from this string and add it to the result.

5. **Add the character to the result**: If the character is not an outermost parenthesis, 
    add it to the result string.

6. **Return the result**: After iterating over the entire input string, return the result string.
"""


print("==============================================")

#solution 2:
def removeOuterParentheses( s: str) -> str:  
        result = []  
        depth = 0  
        
        for char in s:  
            if char == '(':  
                if depth > 0:  
                    result.append(char)  
                depth += 1  
            elif char == ')':  
                depth -= 1  
                if depth > 0:  
                    result.append(char)  
        
        return ''.join(result)  

# Example usage
print(removeOuterParentheses("(()())(())")) 
print(removeOuterParentheses("(()())(())(()(()))"))  
print(removeOuterParentheses("()()")) 
"""Explanation :
Here's what the code does:

1. It initializes an empty list `result` to store the characters that will be part of the final output string.
2. It initializes a variable `depth` to 0. `depth` is used to keep track of the nesting level of the parentheses.
3. It then iterates over each character `char` in the input string `s`.
4. If `char` is an opening parenthesis `(`:
   - It checks if `depth` is greater than 0. If it is, it means we are already inside a set of parentheses, so we append the opening parenthesis to the `result` list.
   - It then increments `depth` by 1.
5. If `char` is a closing parenthesis `)`:
   - It decrements `depth` by 1.
   - If `depth` is still greater than 0 after decrementing, it means we are not at the outermost level of parentheses, so we append the closing parenthesis to the `result` list.
6. Finally, it returns the characters in the `result` list as a string, which represents the input string with its outermost parentheses removed.

**Purpose of `depth`:**

The `depth` variable is used to keep track of the nesting level of the parentheses. It increments when an opening parenthesis is encountered and decrements when a closing parenthesis is encountered.

Here's how `depth` helps:

- When `depth` is 0, it means we are at the outermost level of parentheses, so we do not include the opening or closing parenthesis in the `result` list.
- When `depth` is greater than 0, it means we are inside a set of parentheses (not at the outermost level), so we include the opening or closing parenthesis in the `result` list.

**Why `if depth > 0:` is used:**

The `if depth > 0:` condition is used to filter out the outermost parentheses and only include the inner parentheses in the `result` list.

When the code encounters an opening or closing parenthesis, it checks if `depth` is greater than 0 before including it in the `result` list:

- For an opening parenthesis `(`, if `depth` is 0, it means we are at the outermost level, so we do not include it in the `result` list.
- For a closing parenthesis `)`, if `depth` is 0 after decrementing, it means we have just closed the outermost parentheses, so we do not include it in the `result` list.

By using `if depth > 0:`, we ensure that only the inner parentheses (those not at the outermost level) are included in the `result` list, thus effectively removing the outermost parentheses from the input string.

Here is a simple example to illustrate how `depth` changes:

Input string: `( ( ) )`

1. Initially, `depth` = 0
2. When we encounter the first `(`, `depth` becomes 1. So, we do not include the outermost `(`, but increment `depth`. So, `depth` = 1.
3. When we encounter the second `(`, `depth` becomes 2. We include this `(` because `depth` > 0.
4. When we encounter the `)`, `depth` becomes 1. We include this `)` because `depth` > 0 after decrementing.
5. When we encounter the last `)`, `depth` becomes 0. We do not include this `)`.

So, after processing the entire string, `result` will be `( )`, which is the input string with its outermost parentheses removed.
"""
print("==============================================")

#solution 3:

def removeOuterParentheses(s: str) -> str:
        string = ""
        opened = 0
        for i in s:
            if i == "(":
                opened += 1
                if opened > 1:
                    string += i
            else:
                opened -= 1
                if opened > 0:
                    string += i
        return string

# Example usage
print(removeOuterParentheses("(()())(())")) 
print(removeOuterParentheses("(()())(())(()(()))"))  
print(removeOuterParentheses("()()")) 


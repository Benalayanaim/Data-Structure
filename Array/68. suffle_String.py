#Problem : https://leetcode.com/problems/shuffle-string/description/?envType=problem-list-v2&envId=array




#Solution 1:
def restoreString(s, indices):
    # Create an array of the same length as the input string
    shuffled_string = [''] * len(s)
    
    # Iterate over each character in the string and place it at the correct index
    for i, char in enumerate(s):
        shuffled_string[indices[i]] = char
    
    # Join the list to form the final shuffled string
    return ''.join(shuffled_string)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))

s = "aimn"
indices = [1,2,3,0]
print(restoreString(s, indices))


print("==================================================")

#Solution 2:
def restoreString(s: str, indices: list[int]) -> str:
    
    # Initialize an empty list to store the characters at their correct positions
    shuffled_string = [''] * len(s)
    
    # Iterate over the string and the indices list simultaneously
    for char, index in zip(s, indices):
        # Place each character at its correct position in the shuffled string
        shuffled_string[index] = char
    
    # Join the characters in the shuffled string list into a single string
    result = ''.join(shuffled_string)
    
    return result


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))

s = "aimn"
indices = [1,2,3,0]
print(restoreString(s, indices))

print("==================================================")

#Solution 3:
def restoreString(s, indices):
    shuffled = [''] * len(s)
    for i in range(len(s)):
        shuffled[indices[i]] = s[i]

    return ''.join(shuffled)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))

s = "aimn"
indices = [1,2,3,0]
print(restoreString(s, indices))

print("==================================================")

#Solution 4:
def restoreString(s, indices):
        mydict = {}
        for i in range(len(indices)):
            mydict[indices[i]] = s[i]
        mydict = dict(sorted(mydict.items()))
        result = "".join(mydict.values())
        return result

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))

s = "aimn"
indices = [1,2,3,0]
print(restoreString(s, indices))



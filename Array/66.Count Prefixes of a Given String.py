#Problem : https://leetcode.com/problems/count-prefixes-of-a-given-string/description/?envType=problem-list-v2&envId=array



def countPrefixes(words: list[str], s: str) -> int:
    count = 0
    for word in words:
        if s.startswith(word):
            count += 1
    return count

# Example usage
words = ["a","b","c","ab","bc","abc"]
s = "abc"
print(countPrefixes(words, s))  

words = ["a","a","ba"] 
s = "bo"
#The reason for this output is that none of the words in the `words` list are a prefix of the string `s = "bo"`.  
# Both `"a"` words are not prefixes because they don't match the starting character `"b"`, 
# and `"ba"` is not a prefix because the second character doesn't match.
print(countPrefixes(words, s))  

"""
**Explanation:**

1. Initialize a counter variable `count` to 0.
2. Iterate over each word in the `words` array.
3. For each word, check if the string `s` starts with the current word using the `startswith` method.
4. If `s` starts with the current word, increment the `count` variable.
5. After checking all words, return the `count` variable, which represents the number of strings in `words` that are a prefix of `s`.
"""



print("================================================")

#Solution 2:
def countPrefixes(words, s):
    count=0
    for word in words:
        if (s[:len(word)] == word):
            count+=1
    return count

words = ["a","b","c","ab","bc","abc"]
s = "abc"
print(countPrefixes(words, s))  

words = ["a","a","ba"] 
s = "bo"
print(countPrefixes(words, s))  



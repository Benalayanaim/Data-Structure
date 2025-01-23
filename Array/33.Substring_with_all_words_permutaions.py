"Problem"
#https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/



#solution 1 :
def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])  # Length of each word
    total_len = word_len * len(words)  # Total length of the concatenated string
    word_count = len(words)
    word_freq = {}

    # Build a frequency dictionary for the words
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    result = []

    # Iterate through possible starting indices
    for i in range(len(s) - total_len + 1):
        seen = {}
        j = 0

        # Check substrings in chunks of word length
        while j < word_count:
            start_idx = i + j * word_len
            word = s[start_idx:start_idx + word_len]

            if word in word_freq:
                seen[word] = seen.get(word, 0) + 1

                # If a word appears more than it should, break
                if seen[word] > word_freq[word]:
                    break
            else:
                break

            j += 1

        # If all words matched, record the starting index
        if j == word_count:
            result.append(i)

    return result

# Example 1
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words))  # Output: [0, 9]

# Example 2
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(findSubstring(s, words))  # Output: []

# Example 3
s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(findSubstring(s, words))  # Output: [6, 9, 12]



print("===============================================")

#Solution 2:
def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])  # Length of each word
    word_count = len(words)  # Number of words
    total_len = word_len * word_count  # Total length of the concatenated substring
    word_freq = {}

    # Build a frequency dictionary for the words
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    result = []

    # Iterate through each possible starting position within a single word length
    for start in range(word_len):
        left = start
        right = start
        seen = {}

        while right + word_len <= len(s):
            # Get the current word
            word = s[right:right + word_len]
            right += word_len

            if word in word_freq:
                seen[word] = seen.get(word, 0) + 1

                # If the word frequency exceeds the allowed count, move `left` forward
                while seen[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len

                # If the window size matches `total_len`, add the starting index
                if right - left == total_len:
                    result.append(left)
            else:
                # Reset the window if the word is invalid
                seen.clear()
                left = right

    return result

# Example 1
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words)) 

# Example 2
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(findSubstring(s, words)) 

# Example 3
s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(findSubstring(s, words)) 



print("========================================")
#Solution 3 :
from collections import Counter, defaultdict

def findSubstring(s, words):
    # 1. Initialize necessary variables
    if not s or not words:
        return []
    
    length = len(words[0])  # Length of each word (since all words are of the same length)
    word_count = Counter(words)  # Count the frequency of each word in `words`
    indexes = []  # This will store the starting indices of valid concatenated substrings

    # 2. Loop through possible starting positions (i from 0 to length-1)
    for i in range(length):
        start = i  # Initialize start for the sliding window
        window = defaultdict(int)  # This will keep track of word frequencies in the current window
        words_used = 0  # Count of valid words in the window
        
        # 3. Loop through the string using a sliding window
        for j in range(i, len(s) - length + 1, length):
            word = s[j:j + length]  # Extract the word from the current position
            
            if word not in word_count:
                # If the word is not in `word_count`, reset the window and move start to the next word
                start = j + length
                window = defaultdict(int)
                words_used = 0
                continue

            # Add the current word to the window and increase words_used
            words_used += 1
            window[word] += 1

            # 4. If a word is used more times than it should, shrink the window from the left
            while window[word] > word_count[word]:
                left_word = s[start:start + length]
                window[left_word] -= 1  # Remove the word at the `start` from the window
                start += length  # Move `start` to the next word boundary
                words_used -= 1  # Decrease the count of words used

            # 5. If we used exactly the number of words, add the starting index to the result
            if words_used == len(words):
                indexes.append(start)

    # 6. Return the list of valid starting indices
    return indexes

# Example 1
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words)) 

# Example 2
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(findSubstring(s, words)) 

# Example 3
s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(findSubstring(s, words)) 


print("===================================================")

#Solution 4:
def findSubstring(s, words): 
    # Check if input is empty or invalid
    if not s or not words:
        return []
    
    # Initialize a dictionary to store the frequency of each word in `words`
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    
    lw = len(words[0])  # Length of each word (since all words are of the same length)
    fin = []  # To store the final indices of valid substrings
    
    # Outer loop: Try starting from each position in the string from 0 to len(words[0]) - 1
    for i in range(lw):
        l = r = i  # Initialize the left and right pointers for the sliding window
        window = {}  # To store the frequency of words in the current window
        
        # Inner loop: Move the right pointer and form a sliding window of word-length size
        while r < len(s):
            curr_w = s[r:r + lw]  # Extract the current word (of length `lw`)
            
            # If the word is not in the words list (not in `count`), reset the window
            if curr_w not in count:
                window.clear()  # Clear the window (as this word is not valid)
                r += lw  # Move the right pointer forward by the word length
                l = r  # Move the left pointer to the right pointer
            else:
                # If the word is in `count`, add it to the window
                window[curr_w] = window.get(curr_w, 0) + 1
                
                # If the frequency of the current word is within the allowed count
                if window[curr_w] <= count[curr_w]:
                    r += lw  # Move the right pointer forward by the word length
                else:
                    # If frequency exceeds, shrink the window from the left
                    while l <= r and window[curr_w] > count[curr_w]:
                        w = s[l:l + lw]  # Get the word at the left pointer
                        window[w] -= 1  # Decrease its frequency in the window
                        l += lw  # Move the left pointer to the next word's start
                    r += lw  # Move the right pointer forward by the word length
            
            # If the current window matches the required frequency of words, record the index
            if window == count:
                fin.append(l)  # Append the starting index of the valid substring
    
    return fin

# Example 1
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words)) 

# Example 2
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(findSubstring(s, words)) 

# Example 3
s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(findSubstring(s, words)) 


print("===================================================")

#Another brute force
def findSubstring(s, words):
    if len(words) == 0 or len(s) == 0: return []
    if len(s) < len(''.join(words)): return []
    
    rst = []
    words_cat = ''.join(sorted(words))
    l, m = len(words[0]), len(words)
    l_all = len(words_cat)
    
    for i in range(len(s) - l_all + 1): 
        s_sub = []
        for j in range(m):
            s_sub.append(s[i + l * j : i + l * (j+1)])       
        s_sub = ''.join(sorted(s_sub))
        if s_sub == words_cat: rst.append(i)
    
    return rst 
    
# Example 1
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words)) 

# Example 2
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(findSubstring(s, words)) 

# Example 3
s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(findSubstring(s, words)) 




"Explanation"
"fil chaGPT mte3iiiii"
#https://chatgpt.com/c/676fcc03-72c0-800f-912b-be81bce6bf3e


#Rousource
#https://www.w3schools.com/python/ref_dictionary_get.asp
#https://www.geeksforgeeks.org/defaultdict-in-python/

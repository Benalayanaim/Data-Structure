#Problem
#https://leetcode.com/problems/longest-word-in-dictionary/description/?envType=problem-list-v2&envId=array



"Brute force "

#Solution 
def longestWord( words):
        wordset = set(words)
        words.sort(key = lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word

        return ""

#Example Usage 
words = ["w","wo","wor","worl","world"]
print(longestWord(words))

words = ["a","banana","app","appl","ap","apply","apple"]
print(longestWord(words))

print("=======================================================")

#Solution 2:
def longestWord (words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    ans = word

        return ans

#Example Usage 
words = ["w","wo","wor","worl","world"]
print(longestWord(words))

words = ["a","banana","app","appl","ap","apply","apple"]
print(longestWord(words))



print("=======================================================")

#Solution 3:
def longestWordwords(words) -> str:
        words.sort(reverse=True)
        words.sort(key=len)
        
        # words = set(words)
        currword = ""

        for word in words:
            skip = False
            for i in range(len(word)):
                if not word[:i + 1] in words:
                    skip = True
                    break
            if skip:
                continue
            if len(word) > len(currword):
                currword = word
            if len(word) == len(currword):
                currword = min(word, currword)
            
        return currword

#Example Usage 
words = ["w","wo","wor","worl","world"]
print(longestWord(words))

words = ["a","banana","app","appl","ap","apply","apple"]
print(longestWord(words))


print("============================================")

#Solution5:
def longestWord(self, words) -> str:
        words.sort()

        word_set, ans = set(['']), ''

        for word in words:
            if word[:-1] in word_set:
                if len(word) > len(ans):
                    ans = word
                word_set.add(word)
        
        return ans

#Example Usage 
words = ["w","wo","wor","worl","world"]
print(longestWord(words))

words = ["a","banana","app","appl","ap","apply","apple"]
print(longestWord(words))


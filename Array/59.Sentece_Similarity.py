#Problem
#https://leetcode.ca/2017-12-03-734-Sentence-Similarity/


#Solution 1:
def areSentencesSimilar(sentence1, sentence2, similarPairs):
    # Check if the lengths of the sentences are different
    if len(sentence1) != len(sentence2):
        return False
    
    # Create a set of similar word pairs for quick lookup
    similar_dict = {}
    for x, y in similarPairs:
        if x not in similar_dict:
            similar_dict[x] = set()
        if y not in similar_dict:
            similar_dict[y] = set()
        similar_dict[x].add(y)
        similar_dict[y].add(x)
    
    # Iterate through both sentences and check for similarity
    for word1, word2 in zip(sentence1, sentence2):
        if word1 != word2 and word2 not in similar_dict.get(word1, set()):
            return False
    
    return True

# Example 1
sentence1 = ["great", "acting", "skills"]
sentence2 = ["fine", "drama", "talent"]
similarPairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: True

# Example 2
sentence1 = ["great"]
sentence2 = ["great"]
similarPairs = []
print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: True

# Example 3
sentence1 = ["great"]
sentence2 = ["doubleplus", "good"]
similarPairs = [["great", "doubleplus"]]
print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: False


print("================================================================================")

#Solution 2:
def areSentencesSimilar(sentence1, sentence2, similarPairs):
    # Step 1: Check if sentences have different lengths
    if len(sentence1) != len(sentence2):
        return False  # If lengths differ, they cannot be similar

    # Step 2: Create a set to store all similar pairs
    s = {(a, b) for a, b in similarPairs}

    # Step 3: Check if all word pairs (from the two sentences) are similar
    return all(
        a == b or (a, b) in s or (b, a) in s
        for a, b in zip(sentence1, sentence2)
    )


# Example 1
sentence1 = ["great", "acting", "skills"]
sentence2 = ["fine", "drama", "talent"]
similarPairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: True

# Example 2
sentence1 = ["great"]
sentence2 = ["great"]
similarPairs = []
print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: True

# Example 3
sentence1 = ["great"]
sentence2 = ["doubleplus", "good"]
similarPairs = [["great", "doubleplus"]]
print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: False

print("=================================================================================")

#Solution 3:
def areSentencesSimilar(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False

    similar_words = {}
    for word1, word2 in similarPairs:
        if word1 not in similar_words:
            similar_words[word1] = set()
        if word2 not in similar_words:
            similar_words[word2] = set()
        similar_words[word1].add(word2)
        similar_words[word2].add(word1)

    for word1, word2 in zip(sentence1, sentence2):
        if word1 == word2:
            continue
        if word1 not in similar_words or word2 not in similar_words.get(word1, set()):
            return False

    return True

# Example 1
sentence1 = ["great", "acting", "skills"]
sentence2 = ["fine", "drama", "talent"]
similarPairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: True

# Example 2
sentence1 = ["great"]
sentence2 = ["great"]
similarPairs = []
print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: True

# Example 3
sentence1 = ["great"]
sentence2 = ["doubleplus", "good"]
similarPairs = [["great", "doubleplus"]]
print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: False







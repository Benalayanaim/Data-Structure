#Problem
#https://leetcode.ca/2016-07-31-244-Shortest-Word-Distance-II/
#https://www.youtube.com/watch?v=MR52ptzetSQ




#Solution 1:
from typing import List

class WordDistance:
    def __init__(self, wordsDict: List[str]):
        # Build a mapping from word to all indices where it appears
        self.word_indices = {}
        for index, word in enumerate(wordsDict):
            if word not in self.word_indices:
                self.word_indices[word] = []
            self.word_indices[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        # Retrieve the lists of indices for word1 and word2
        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]
        
        # Two pointers to iterate through the two lists
        i, j = 0, 0
        min_dist = float('inf')
        
        # Move through both lists to find the smallest difference
        while i < len(indices1) and j < len(indices2):
            pos1, pos2 = indices1[i], indices2[j]
            min_dist = min(min_dist, abs(pos1 - pos2))
            
            # Move the pointer that points to the smaller index
            if pos1 < pos2:
                i += 1
            else:
                j += 1
                
        return min_dist

# Example usage:
if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    wd = WordDistance(words)
    print(wd.shortest("coding", "practice")) 
    print(wd.shortest("makes", "coding"))     



#Explanation fy chat mte3ii: https://chatgpt.com/c/679f8706-ee44-800f-bc9c-c8b671b71f74


print("===========================================================================")

#Solution 2:
from collections import defaultdict

class WordDistance:
    def __init__(self, wordsDict):
        self.word_indices = defaultdict(list)
        for index, word in enumerate(wordsDict):
            self.word_indices[word].append(index)

    def shortest(self, word1, word2):
        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]
        min_distance = float('inf')
        i, j = 0, 0
        
        # Use two pointers to find the minimum distance
        while i < len(indices1) and j < len(indices2):
            min_distance = min(min_distance, abs(indices1[i] - indices2[j]))
            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1
        
        return min_distance

# Example usage:
wordDistance = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print(wordDistance.shortest("coding", "practice"))  
print(wordDistance.shortest("makes", "coding"))     




print("===========================================================================")

#Solution 3
from typing import List

class WordDistance:
    def __init__(self, wordsDict: List[str]):
        """
        Initializes the WordDistance object with the given list of words.

        :param wordsDict: The list of words.
        """
        self.words_dict = wordsDict
        self.word_to_indices = {word: [i for i, x in enumerate(wordsDict) if x == word] for word in set(wordsDict)}

    def shortest(self, word1: str, word2: str) -> int:
        """
        Returns the shortest distance between word1 and word2 in the list.

        :param word1: The first word.
        :param word2: The second word.
        :return: The shortest distance between word1 and word2.
        """
        if len(self.word_to_indices[word1]) == 0 or len(self.word_to_indices[word2]) == 0:
            return -1  # word1 or word2 not found in the list

        indices1 = self.word_to_indices[word1]
        indices2 = self.word_to_indices[word2]

        min_distance = float('inf')
        for idx1 in indices1:
            for idx2 in indices2:
                if idx1 != idx2:
                    min_distance = min(min_distance, abs(idx1 - idx2))

        return min_distance


# Example usage:
if __name__ == "__main__":
    word_distance = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print(word_distance.shortest("coding", "practice"))  
    print(word_distance.shortest("makes", "coding"))  

### Explanation

"""1. The `WordDistance` class is initialized with a list of strings `wordsDict`.
2. The `word_to_indices` dictionary is created to store the indices of each word in the list.
3. The `shortest` method takes two words `word1` and `word2` as input and returns the shortest distance between them in the list.
4. The method first checks if both words are present in the list. If not, it returns -1.
5. It then iterates over the indices of both words and calculates the absolute difference between each pair of indices.
6. The minimum distance is updated and returned as the result."""

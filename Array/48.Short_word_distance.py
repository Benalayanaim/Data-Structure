#Problem 
#https://leetcode.ca/2016-07-30-243-Shortest-Word-Distance/


"Same problem but in text not in array : https://www.geeksforgeeks.org/minimum-distance-between-words-of-a-string/"


#Solution 1:
def shortestDistance(wordsDict, word1, word2):
    # Initialize indices for the positions of word1 and word2
        index1 = index2 = -1
        # Initialize the answer as infinite to ensure any actual distance found is smaller
        shortest_distance = float('inf')
      
        # Loop through the words in the dictionary to find the closest distance
        for index, word in enumerate(wordsDict):
            if word == word1:
                index1 = index  # Update the position of word1
            if word == word2:
                index2 = index  # Update the position of word2
              
            # If both words have been found at least once, calculate the distance
            if index1 != -1 and index2 != -1:
                distance = abs(index1 - index2)  # Compute absolute difference
                shortest_distance = min(shortest_distance, distance)  # Update the shortest distance
      
        # Return the shortest distance found between the two words
        return shortest_distance

# Example usage
wordsDict1 = ["practice", "makes", "perfect", "coding", "makes"]
word1_1, word2_1 = "coding", "practice"
print(shortestDistance(wordsDict1, word1_1, word2_1))  

wordsDict2 = ["practice", "makes", "perfect", "coding", "makes"]
word1_2, word2_2 = "makes", "coding"
print(shortestDistance(wordsDict2, word1_2, word2_2))  






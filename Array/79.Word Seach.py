#Problem
#https://leetcode.com/problems/word-search/description/?envType=problem-list-v2&envId=array



#Solution1 :
def exist(board, word):
    def backtrack(i, j, index):
        # If we have matched all characters in the word
        if index == len(word):
            return True
        
        # Check if the current cell is out of bounds or doesn't match the current character
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False
        
        # Temporarily mark the current cell as visited
        temp = board[i][j]
        board[i][j] = '#'
        
        # Explore all four possible directions
        if (backtrack(i + 1, j, index + 1) or
            backtrack(i - 1, j, index + 1) or
            backtrack(i, j + 1, index + 1) or
            backtrack(i, j - 1, index + 1)):
            return True
        
        # Backtrack: unmark the current cell
        board[i][j] = temp
        return False
    
    # Iterate over each cell in the grid to start the search
    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True
    
    return False

# Example usage:
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"

print(exist(board, word1))  
print(exist(board, word2))  
print(exist(board, word3))  

#Expalanation : https://chat.deepseek.com/a/chat/s/75616a23-f466-4a00-9a43-26404e54acff


print("=======================================================")


#Solution 2:

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    if not board or not board[0]:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
            return False
        
        temp, board[r][c] = board[r][c], "#"  # Mark the cell as visited
        
        found = (dfs(r + 1, c, index + 1) or
                 dfs(r - 1, c, index + 1) or
                 dfs(r, c + 1, index + 1) or
                 dfs(r, c - 1, index + 1))
        
        board[r][c] = temp  # Restore the cell back
        return found
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    
    return False

# Example usage
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"

print(exist(board, word1))  
print(exist(board, word2))  
print(exist(board, word3))  


#Explanation mi chat mte3iii : https://chatgpt.com/c/679fcc97-750c-800f-8116-cf171bfd37d8
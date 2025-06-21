#Problem 
#https://leetcode.com/problems/unique-paths/description/



"Code DP - 2D"
#Solution 1:
def uniquePaths(m: int, n: int) -> int:
    # Create a 2D DP table initialized with 1s
    dp = [[1] * n for _ in range(m)]
    
    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # The bottom-right corner will have the total number of unique paths
    return dp[m-1][n-1]

# Example usage:
print(uniquePaths(3, 7))  
print(uniquePaths(3, 2))  


"Explanation "
#https://chat.deepseek.com/a/chat/s/f621a813-18df-4861-8939-91525dcb64de



"Code DP - 1D"

print("==================================================")
#Solution 2:
def uniquePaths(m, n): 
        curr_row = [1] * n
        prev_row = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                curr_row[j] = curr_row[j - 1] + prev_row[j]    
            curr_row, prev_row = prev_row, curr_row
        
        return prev_row[-1]

# Example usage:
print(uniquePaths(3, 7))  
print(uniquePaths(3, 2))  

"Explanation"
# Mi chat Mte3iii : https://chatgpt.com/c/679fb636-7c58-800f-8bed-0a5d2cc72152

#https://chat.deepseek.com/a/chat/s/f621a813-18df-4861-8939-91525dcb64de




print("==================================================")
#Solution 3
import math
def uniquePaths(m: int, n: int) -> int:
    return math.comb(m+n-2, m-1)

# Example usage:
print(uniquePaths(3, 7))  
print(uniquePaths(3, 2))  

"Explanation"
## Mi chat Mte3iii : https://chatgpt.com/c/679fb636-7c58-800f-8bed-0a5d2cc72152



"""Another Explanation for all solution
https://leetcode.com/problems/unique-paths/solutions/3994523/98-83-easy-dp-math/"""

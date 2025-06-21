#Problem :
#https://leetcode.com/problems/minimum-path-sum/description/?envType=problem-list-v2&envId=array






#Solution 1:
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[0][0] = grid[0][0]
    
    # Fill the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill the first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill the rest of the table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

# Example usage:
grid1 = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]
print(minPathSum(grid1))  

grid2 = [
  [1, 2, 3],
  [4, 5, 6]
]
print(minPathSum(grid2))  



grid3 = [
    [1, 2, 3],
    [4, 5, 6],
    [5, 5, 6]
    ]
print(minPathSum(grid3))


print("==============================================================")

#Solution 2:

def minPathSum(grid):
        
        m, n = len(grid), len(grid[0])
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]

# Example usage:
grid1 = [ [1, 3, 1],[1, 5, 1],[4, 2, 1]]
print(minPathSum(grid1))  

grid2 = [[1, 2, 3],[4, 5, 6]]
print(minPathSum(grid2))  

grid3 = [[1, 2, 3],[4, 5, 6],[5, 5, 6]]
print(minPathSum(grid3))  



#Explanation : https://chat.deepseek.com/a/chat/s/26075626-4567-411b-aa34-1b58e9d6c1c1

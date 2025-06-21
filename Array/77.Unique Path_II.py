#Problem 
#https://leetcode.com/problems/unique-paths-ii/description/?envType=problem-list-v2&envId=array





#Solution 1:
def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    
    # If the starting cell is an obstacle, no paths exist
    if obstacleGrid[0][0] == 1:
        return 0
    
    # Initialize DP table
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    
    # Fill the first row
    for j in range(1, n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = dp[0][j-1]
    
    # Fill the first column
    for i in range(1, m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = dp[i-1][0]
    
    # Fill the rest of the DP table
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# Example usage:
obstacleGrid1 = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid1))  

obstacleGrid2 = [[0,1],[0,0]]
print(uniquePathsWithObstacles(obstacleGrid2))  



print("========================================================")

#Solution 2:
def uniquePathsWithObstacles(obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        previous = [0] * n
        current = [0] * n
        previous[0] = 1
        
        for i in range(m):
            current[0] = 0 if obstacleGrid[i][0] == 1 else previous[0]
            for j in range(1, n):
                current[j] = 0 if obstacleGrid[i][j] == 1 else current[j-1] + previous[j]
            previous[:] = current
        
        return previous[n-1]



# Example usage:
obstacleGrid1 = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid1))  

obstacleGrid2 = [[0,1],[0,0]]
print(uniquePathsWithObstacles(obstacleGrid2))  

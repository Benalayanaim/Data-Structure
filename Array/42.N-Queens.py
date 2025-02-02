#Problem : https://leetcode.com/problems/n-queens/description/




#Solution 1:
def solveNQueens(n):
    def is_safe(row, col, diagonals, anti_diagonals, cols):
        """Check if placing a queen at (row, col) is safe."""
        return col not in cols and (row - col) not in diagonals and (row + col) not in anti_diagonals

    def place_queen(row, col, board, diagonals, anti_diagonals, cols):
        """Place a queen on the board and update helper sets."""
        board[row][col] = "Q"
        cols.add(col)
        diagonals.add(row - col)
        anti_diagonals.add(row + col)

    def remove_queen(row, col, board, diagonals, anti_diagonals, cols):
        """Remove a queen from the board and update helper sets."""
        board[row][col] = "."
        cols.remove(col)
        diagonals.remove(row - col)
        anti_diagonals.remove(row + col)

    def backtrack(row):
        """Recursive backtracking to place queens row by row."""
        if row == n:
            # Add the current board configuration to solutions
            solutions.append(["".join(r) for r in board])
            return
        
        for col in range(n):
            if is_safe(row, col, diagonals, anti_diagonals, cols):
                # Place queen and proceed to the next row
                place_queen(row, col, board, diagonals, anti_diagonals, cols)
                backtrack(row + 1)
                # Backtrack by removing the queen
                remove_queen(row, col, board, diagonals, anti_diagonals, cols)

    # Initialize variables
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []
    cols = set()  # Tracks columns where queens are placed
    diagonals = set()  # Tracks top-left to bottom-right diagonals
    anti_diagonals = set()  # Tracks top-right to bottom-left diagonals

    # Start backtracking from the first row
    backtrack(0)
    return solutions


# Test Cases
n = 4
print(solveNQueens(n))

print("=============================================")

#Solution 2:
def solveNQueens1(n): 
        def dfs(row, cols, diag1, diag2, board) -> None:
            if row == n:
                solutions.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                dfs(row + 1, cols, diag1, diag2, board)
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        solutions = []
        board = [['.'] * n for _ in range(n)]
        dfs(0, set(), set(), set(), board)
        return solutions

n = 4
print(solveNQueens1(n))


print("=============================================")

#Solution 3:
def solveNQueens3(n): 
        
        if n == 0: return []
        
        col = set()
        diagonal = set()    # determined by r+c
        antidiagonal = set() #
        output = []
        result = []
        
        def backtrack(r):
            nonlocal n,col,diagonal,antidiagonal,output,result
            if r == n:
                result.append(output[:])
                return
            
            for c in range(n):
                if c in col or (r+c) in diagonal or (r-c) in antidiagonal: continue
                
                col.add(c)
                diagonal.add(r+c)
                antidiagonal.add(r-c)
                output.append('.'*c + 'Q' + '.'*(n-c-1))
                backtrack(r+1)
                
                col.remove(c)
                diagonal.remove(r+c)
                antidiagonal.remove(r-c)
                output.pop()
        
        backtrack(0)
        return result


n = 4
print(solveNQueens3(n))

"""Explanation: 

Runtime: 52 ms, faster than 95.31% of Python3 online submissions for N-Queens.
Memory Usage: 14.3 MB, less than 26.71% of Python3 online submissions for N-Queens.

Goal: Place a queen somewhere such that no queen are attacking each other
Approach: backtracking
- each recursive layer will decide on a row and also the placement of the queen
- the constraint is making sure we do not place a queen where its in sight of another queen. How?
    1) make sure it is not on the same column --> create a column set
    2) make sure it is not in same diagonal path --> create a diagonal set (calculated via r+c)
    3) make sure it is not in a antidiagonal path --> create a antidiagonal set (calculated via r-c)
    
    We dont need to worry about rows because it is handled by the backtracking parameter that always recurse
    to next level of the row
    
    ** note: if you dont know why r+c and r-c are diagonal paths --> Draw it out and check why it does!! 
    

"""


#Explanation : https://chatgpt.com/c/677e51be-0b98-800f-992f-d522cb04a94b
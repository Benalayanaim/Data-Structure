#https://leetcode.com/problems/n-queens-ii/description/




#Solution :

def totalNQueens(n: int) -> int:
    def backtrack(row: int, cols: set, diagonals: set, anti_diagonals: set) -> int:
        # Base case: If all queens are placed, count this as a solution
        if row == n:
            return 1
        
        solutions = 0
        for col in range(n):
            diagonal = row - col
            anti_diagonal = row + col
            # Check if this position is under attack
            if col in cols or diagonal in diagonals or anti_diagonal in anti_diagonals:
                continue
            
            # Place the queen
            cols.add(col)
            diagonals.add(diagonal)
            anti_diagonals.add(anti_diagonal)
            
            # Recurse to the next row
            solutions += backtrack(row + 1, cols, diagonals, anti_diagonals)
            
            # Backtrack: Remove the queen
            cols.remove(col)
            diagonals.remove(diagonal)
            anti_diagonals.remove(anti_diagonal)
        
        return solutions
    
    return backtrack(0, set(), set(), set())

# Example usage:
print(totalNQueens(4))  
print(totalNQueens(1))  



"Explanation : https://chatgpt.com/c/677fc1b1-21a8-800f-a50a-797e569854cb"


"What is ant_diagnoal : https://www.google.com/search?q=antidiagonale+matrice&rlz=1C1CHBD_frTN1087TN1087&oq=antidiago&gs_lcrp=EgZjaHJvbWUqBwgBEAAYgAQyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIICAMQABgKGB4yCAgEEAAYChgeMgYIBRAAGB4yBggGEAAYHjIICAcQABgKGB4yCAgIEAAYChgeMgYICRAAGB7SAQkxMzY5MmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8#vhid=CnQ7-qmAtmIvbM&vssid=l"
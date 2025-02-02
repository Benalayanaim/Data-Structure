"Problem : https://leetcode.com/problems/sudoku-solver/description/"



#Solution 1:

def solve_sudoku(board):
    def is_valid(row, col, num):
        # Check if the number is already in the row
        for i in range(9):
            if board[row][i] == num:
                return False

        # Check if the number is already in the column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check if the number is in the 3x3 sub-grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':  # Find an empty cell
                    for num in map(str, range(1, 10)):  # Try digits '1' to '9'
                        if is_valid(i, j, num):
                            board[i][j] = num  # Place the number
                            if backtrack():  # Recursively solve the rest
                                return True
                            board[i][j] = '.'  # Undo placement
                    return False  # If no number is valid, backtrack
        return True

    backtrack()


# Example usage
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

solve_sudoku(board)

# Output the solved Sudoku board
for row in board:
    print(row)













print("==============================================")

#Solution 2:
def solveSudoku1(board): 
        """
        Do not return anything, modify board in-place instead.
        """
        unsolved = []
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": 
                    unsolved.append((i, j))
                else: 
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    square[i//3*3+j//3].add(board[i][j])
                    
        def backtrack(index):
            if index == len(unsolved): 
                return True
            
            min_candidate = 10
            min_index = index
            for x in range(index, len(unsolved)):
                i, j = unsolved[x]
                box_index = (i // 3) * 3 + (j // 3)
                possible = {'1','2','3','4','5','6','7','8','9'} - row[i] - col[j] - square[box_index]
                candidates = len(possible)
                if candidates < min_candidate:
                    min_candidate = candidates
                    min_index = x
                if min_candidate == 1:
                    break 
            
            unsolved[index], unsolved[min_index] = unsolved[min_index], unsolved[index]
            i, j = unsolved[index]
            box_index = (i // 3) * 3 + (j // 3)
            possible_numbers = {'1','2','3','4','5','6','7','8','9'} - row[i] - col[j] - square[box_index]

            for num in possible_numbers:
                board[i][j] = num
                row[i].add(num)
                col[j].add(num)
                square[i//3*3+j//3].add(num)
                if backtrack(index+1): 
                    return True
                row[i].remove(num)
                col[j].remove(num)
                square[i//3*3+j//3].remove(num)
                board[i][j] = '.'
            return False 
        
        backtrack(0)


# Example usage
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

solveSudoku1(board)

# Output the solved Sudoku board
for row in board:
    print(row)



#Explanation : https://chatgpt.com/c/677d15da-49c8-800f-b435-ee142922f456

"set()"
#https://www.geeksforgeeks.org/python-set-function/
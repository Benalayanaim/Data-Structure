#https://leetcode.com/problems/game-of-life/description/

#https://chatgpt.com/c/675dfa65-ae04-8007-9407-33be58ab00e2



#Solution N1:
def game_of_life(board):
    # Dimensions of the board
    m, n = len(board), len(board[0])

    # Function to count live neighbors of a cell at (row, col)
    def count_live_neighbors(row, col):
        live_neighbors = 0
        # Check all 8 directions (top-left, top, top-right, left, right, bottom-left, bottom, bottom-right)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Above row
            (0, -1),         (0, 1),     # Same row
            (1, -1), (1, 0), (1, 1)      # Below row
        ]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            # Check if the neighbor is within bounds and is alive
            if 0 <= r < m and 0 <= c < n and board[r][c] == 1:
                live_neighbors += 1
        return live_neighbors

    # Make a copy of the board to calculate the next state
    next_board = [[0] * n for _ in range(m)]

    # Loop through each cell in the board
    for row in range(m):
        for col in range(n):
            # Count the live neighbors for the current cell
            live_neighbors = count_live_neighbors(row, col)

            # Apply the rules of the Game of Life
            if board[row][col] == 1:  # If the cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    next_board[row][col] = 0  # Cell dies
                else:
                    next_board[row][col] = 1  # Cell survives
            else:  # If the cell is dead
                if live_neighbors == 3:
                    next_board[row][col] = 1  # Cell becomes alive

    # Update the original board with the next state
    for row in range(m):
        for col in range(n):
            board[row][col] = next_board[row][col]


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
game_of_life(board)
print(board)

board1 = [[1,1],[1,0]]
game_of_life(board1)
print(board1)


print("==================================")

#Solution 2:
def gameOfLife(board) :
        """
        Do not return anything, modify board in-place instead.
        """
        ## RC ##
        ## APPRAOCH : IN-PLACE MANIPULATION ##
        #  when the value needs to be updated, we donot just change  0 to 1 / 1 to 0 but we do in increments and decrements of 2. (table explains)        
        ##   previous value state change  current state   current value
        ##   0              no change     dead            0
        ##   1              no change     live            1
        ##   0              changed (+2)  live            2
        ##   1              changed (-2)  dead            -1
        
		## TIME COMPLEXITY : O(MxN) ##
		## SPACE COMPLEXITY : O(1) ##

        directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0                # live neighbors count
                for x, y in directions: # check and count neighbors in all directions
                    if ( i + x < len(board) and i + x >= 0 ) and ( j + y < len(board[0]) and j + y >=0 ) and abs(board[i + x][j + y]) == 1:
                        live += 1
                if board[i][j] == 1 and (live < 2 or live > 3):     # Rule 1 or Rule 3
                    board[i][j] = -1
                if board[i][j] == 0 and live == 3:                  # Rule 4
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if(board[i][j] > 0) else 0
        return board

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
gameOfLife(board)
print(board)

board1 = [[1,1],[1,0]]
gameOfLife(board1)
print(board1)


print("==============================")

#this the optimize solution for the fromthe sol2:

#solution 3:
def gameOfLife_optimize(board):
    """
    Do not return anything, modify board in-place instead.
    """
    # Directions to check the 8 neighbors
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    rows, cols = len(board), len(board[0])

    # Step 1: Iterate through the board to determine the next state
    for i in range(rows):
        for j in range(cols):
            # Count live neighbors
            live_neighbors = 0
            for dr, dc in directions:
                r, c = i + dr, j + dc
                if 0 <= r < rows and 0 <= c < cols and abs(board[r][c]) == 1:
                    live_neighbors += 1
            
            # Apply rules:
            # Rule 1 & 3: Alive cell dies
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = -1
            # Rule 4: Dead cell becomes alive
            if board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 2

    # Step 2: Finalize the board by converting intermediate states
    for i in range(rows):
        for j in range(cols):
            # Convert intermediate states back to final states
            board[i][j] = 1 if board[i][j] > 0 else 0

    return board

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
gameOfLife_optimize(board)
print(board)

board1 = [[1,1],[1,0]]
gameOfLife_optimize(board1)
print(board1)


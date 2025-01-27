#Problem : https://leetcode.com/problems/valid-sudoku/description/






#Solution 1:

def isValidSudoku(board):
    # Helper function to check if a list contains duplicates (ignoring '.')
    def hasDuplicates(nums):
        seen = set()
        for num in nums:
            if num != '.' and num in seen:
                return True
            seen.add(num)
        return False

    # Check rows
    for row in board:
        if hasDuplicates(row):
            return False

    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if hasDuplicates(column):
            return False

    # Check 3x3 sub-boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            sub_box = [
                board[row][col]
                for row in range(box_row, box_row + 3)
                for col in range(box_col, box_col + 3)
            ]
            if hasDuplicates(sub_box):
                return False

    return True

# Example 1
board1 = [
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
print(isValidSudoku(board1))

# Example 2
board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board2))  





print("===================================================")

#Solution 2:

def isValidSudoku(board):
    res = []
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element != '.':
                res += [(i, element), (element, j), (i // 3, j // 3, element)]
    return len(res) == len(set(res))

# Example 1
board1 = [
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
print(isValidSudoku(board1))

# Example 2
board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board2))  


""" Explanation :
1)It initializes an empty list called "res", which will be used to store all the valid elements in the board.

2)It loops through each cell in the board using two nested "for" loops.
For each cell, it retrieves the value of the element in that cell and stores it in a variable called "element".

3)If the element is not a dot ('.'), which means it's a valid number, the method adds three tuples to the "res" list:

        The first tuple contains the row index (i) and the element itself.
        The second tuple contains the element itself and the column index (j).
        The third tuple contains the floor division of the row index by 3 (i // 3), 
        the floor division of the column index by 3 (j // 3), and the element itself. 
        This tuple represents the 3x3 sub-grid that the current cell belongs to.

4)After processing all the cells, the method checks if the length of "res" is equal to the length of the set of "res".
"""




print("===================================================")

#Solution 3:
def isValidSudoku(board): 
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
    
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                box_index = (i // 3) * 3 + (j // 3)
                if num in rows[i] or num in columns[j] or num in boxes[box_index]:
                    return False
                rows[i].add(num)
                columns[j].add(num)
                boxes[box_index].add(num)
        return True


# Example 1
board1 = [
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
print(isValidSudoku(board1))

# Example 2
board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board2))  





print("===================================================")

#Solution 4:

from collections import defaultdict
def isValidSudoku(board): 
        ROWS, COLS = len(board), len(board[0])
        col_dict = defaultdict(set)
        box_dict = defaultdict(set)
        row_dict = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val==".":
                    continue
                box_key = r//3, c//3

                if val in col_dict[c]: 
                    #print("col",r,c,val)
                    return False
                else: col_dict[c].add(val)
                
                if val in row_dict[r]:
                    #print("row",r,c,val)
                    return False
                else: row_dict[r].add(val)

                if val in box_dict[box_key]: 
                    #print("box",r,c,val)
                    return False
                else: box_dict[box_key].add(val)

        return True


# Example 1
board1 = [
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
print(isValidSudoku(board1))

# Example 2
board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board2))  



#Explanation : https://chatgpt.com/c/677bb6b4-df60-800f-b301-efe66623e6cb

"Resource :"
"when I should use helper function"
    #https://www.google.com/search?q=when+I+should+use+helper+function&sca_esv=16665a235f9aa043&rlz=1C1CHBD_frTN1087TN1087&sxsrf=ADLYWIK3l2MHvYfN9-Gp_0uTFyDH-VS9WQ%3A1736161879391&ei=V7p7Z4jJF-629u8P1_ur4Ac&ved=0ahUKEwjI0N-A--CKAxVum_0HHdf9CnwQ4dUDCA8&uact=5&oq=when+I+should+use+helper+function&gs_lp=Egxnd3Mtd2l6LXNlcnAiIXdoZW4gSSBzaG91bGQgdXNlIGhlbHBlciBmdW5jdGlvbjIFECEYoAFIuUZQAFi9QXAAeAGQAQCYAawBoAGjIKoBBDAuMzO4AQPIAQD4AQGYAiGgArwhwgIMECMYgAQYExgnGIoFwgIKECMYgAQYJxiKBcICChAAGIAEGEMYigXCAhAQABiABBixAxhDGIMBGIoFwgIREC4YgAQYsQMY0QMYgwEYxwHCAgsQABiABBixAxiDAcICDhAuGIAEGLEDGNEDGMcBwgIEECMYJ8ICCxAuGIAEGLEDGIMBwgIOEC4YgAQYsQMYgwEYigXCAggQABiABBixA8ICBRAAGIAEwgIEEAAYA8ICGhAuGIAEGLEDGIMBGJcFGNwEGN4EGOAE2AEBwgIOEAAYgAQYsQMYgwEYigXCAggQABiABBjLAcICCBAuGIAEGMsBwgIFEC4YgATCAhcQLhiABBjLARiXBRjcBBjeBBjgBNgBAcICFBAuGIAEGJcFGNwEGN4EGOAE2AEBwgIKEAAYgAQYChjLAcICBhAAGBYYHsICCBAAGBYYChgewgIFEAAY7wXCAggQABiABBiiBMICBxAhGKABGArCAgQQIRgVwgIFECEYnwWYAwC6BgYIARABGBSSBwQwLjMzoAef3QE&sclient=gws-wiz-serp
"for _ in python"
    #https://www.datacamp.com/tutorial/role-underscore-python
    #https://www.geeksforgeeks.org/underscore-_-python/
"Underscore (_) in Python"
    #https://www.geeksforgeeks.org/defaultdict-in-python/


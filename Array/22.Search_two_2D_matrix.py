"Problem"
#https://leetcode.com/problems/search-a-2d-matrix/description/






#Solution 1 :
def search_target__in_matrix(matrix, target):

    r = len(matrix)
    c = len(matrix[0])

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == target:
                return True
    

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 3

print(search_target__in_matrix(matrix, target))


print("==================================")

#Solution N2:
#see the explanation in chat and focus in the walkthrough example to understand the Divmod

def searchMatrixx(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Map 1D index to 2D matrix
        row, col = divmod(mid, n)
        mid_value = matrix[row][col]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 3

print(searchMatrixx(matrix, target))

#Resource : https://www.w3schools.com/python/ref_func_divmod.asp
#Resource : https://www.geeksforgeeks.org/divmod-python-application/
#Resource : https://www.programiz.com/python-programming/methods/built-in/divmod

print("==================================")

"""Solution withou DIVMOD"""
#Solution N3:
def searchMatrix(matrix: list, target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2

        # Calculate the row and column indices
        row = mid // cols
        col = mid % cols

        # Access the matrix value at the computed row and column
        mid_value = matrix[row][col]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


print("==================================")

#Solution N4:
def searchMatrix(matrix: list, target: int) -> bool:
    return any(target in row for row in matrix)

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 3

print(searchMatrix(matrix, target))



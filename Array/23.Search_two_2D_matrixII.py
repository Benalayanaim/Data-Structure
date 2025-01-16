"Problem : "
#https://leetcode.com/problems/search-a-2d-matrix-ii/description/

"Explanation :"
#
#https://chatgpt.com/c/675d69d8-7cac-8007-bcf9-cd2c897984ba


#Solution : 1

def searchMatrix1(matrix, target):
    # Iterate over each row
    for row in matrix:
        # Iterate over each element in the row
        for element in row:
            # Check if the current element matches the target
            if element == target:
                return True
    # If we finish the loops and don't find the target, return False
    return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 5
print(searchMatrix1(matrix, target))  # Output: True


target = 20
print(searchMatrix1(matrix, target))  # Output: False


print("====================================")

#Solution : 2
def searchMatrix2(matrix, target):
    if not matrix or not matrix[0]:
        return False

    # Get dimensions of the matrix
    m, n = len(matrix), len(matrix[0])

    # Start at the top-right corner
    row, col = 0, n - 1

    # While we are within bounds of the matrix
    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False  # If we exit the loop, the target is not in the matrix


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrix2(matrix, target))  

# Example 2
target = 20
print(searchMatrix2(matrix, target))  

print("====================================")

#Solution : 3

def searchMatrix3(matrix, target) -> bool:
        # set initial position to top right corner
        row, col = 0, len(matrix[0])-1
        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                # target found
                return True
            elif matrix[row][col] < target:
                # current element is smaller than target, move down one row
                row += 1
            else:
                # current element is greater than target, move left one column
                col -= 1
                
        # target not found
        return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrix3(matrix, target))  

# Example 2
target = 20
print(searchMatrix3(matrix, target))  

"""Approach
The problem can be solved using a divide and conquer approach. We start from the top right corner and move towards the bottom left corner 
of the matrix. At each position, we check if the current element is equal to the target value. If it is equal, we return True. 
If it is less than the target value, we move down one row because all the elements in the current row are smaller than the current element. 
If it is greater than the target value, we move left one column because all the elements in the current column are greater than the current 
element.

The time complexity of this algorithm is O(m+n) because in the worst case scenario we traverse all rows and columns. The space complexity 
is O(1) because we are not using any extra data structure."""

print("====================================")


#Solution : 4

def searchMatrix4(matrix, target) -> bool:
    # Iterate through each row in the matrix
    for row in matrix:
        # Use the `in` operator to check if the target exists in the current row
        if target in row:
            return True

    # If no match is found in any row, return False
    return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrix4(matrix, target)) 


target = 20
print(searchMatrix4(matrix, target))

print("====================================")

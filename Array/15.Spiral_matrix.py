#Leetcode : https://leetcode.com/problems/spiral-matrix/

#Explanation 3 solutions : https://chatgpt.com/c/6752ce95-2b08-8007-9faa-93febcd20eec






#Solution 1:
def spiralOrder(matrix):
    res = []

    if len(matrix) == 0 : 
        return res
    
    row_begin = 0
    col_begin = 0

    row_end = len(matrix) - 1
    col_end = len(matrix[0]) - 1

    while (row_begin <= row_end and col_begin <= col_end):
        for i in range(col_begin, col_end + 1):
            res.append(matrix[row_begin][i])
        row_begin += 1

        for i in range(row_begin, row_end + 1):
            res.append(matrix[i][col_end])
        col_end -= 1

        if (row_begin <= row_end):
            for i in range(col_end, col_begin - 1 , -1):
                res.append(matrix[row_end][i])
            row_end -= 1
        
        if(col_begin <= col_end):
            for i in range(row_end, row_begin - 1, -1):
                res.append(matrix[i][col_begin])
            col_begin += 1
    
    return res


# Example Usage
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(spiralOrder(matrix1))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiralOrder(matrix2))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


print("=========================================")
#Solution 2:

def spiralorder(matrix):
    result = []

    while matrix:
        result += matrix.pop(0) #1

        if matrix and matrix[0]: #2
            for line in matrix:
                result.append(line.pop())

        if matrix: #3
            result += matrix.pop()[::-1]

        if matrix and matrix[0]: #4
            for line in matrix[::-1]:
                result.append(line.pop(0))

    return result

# Example Usage
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(spiralorder(matrix1))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiralorder(matrix2))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


#Explanation clear here :  https://leetcode.com/problems/spiral-matrix/solutions/3039684/python-solution-explained-step-by-step-with-illustrations/
print("=========================================")

#Solution 3:

def spiralOrder1(matrix):
    return (
        matrix
        and [*matrix.pop(0)]  # Step 1: Take the first row
        + spiralOrder([*zip(*matrix)][::-1])  # Step 2: Rotate and recurse
    )

# Example Usage
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(spiralOrder1(matrix1))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiralOrder1(matrix2)) 

#Explanation clear here : https://leetcode.com/problems/spiral-matrix/solutions/20571/1-liner-in-python-ruby/
#Problem
#https://leetcode.com/problems/reshape-the-matrix/description/



#Solution 1:
def matrixReshape(mat, r, c):
    # Get the original dimensions of the matrix
    m, n = len(mat), len(mat[0])
    
    # Check if reshape is possible
    if m * n != r * c:
        return mat  # Return the original matrix if reshape is not possible
    
    # Flatten the original matrix into a 1D list
    flattened = [element for row in mat for element in row]
    
    # Reshape the flattened list into the new r x c matrix
    reshaped = []
    for i in range(r):
        # Calculate the start and end indices for each row in the reshaped matrix
        start = i * c
        end = start + c
        reshaped.append(flattened[start:end])
    
    return reshaped

# Example usage:
mat1 = [[1, 2], [3, 4]]
r1, c1 = 1, 4
print(matrixReshape(mat1, r1, c1))  

mat2 = [[1, 2], [3, 4]]
r2, c2 = 2, 4
print(matrixReshape(mat2, r2, c2))  


print("==============================================================")

#Solution 2:
def matrixReshape(mat, r, c):
        # counter = 0
        rows = len(mat)
        cols = len(mat[0])
        if r * c != rows * cols:
            return mat
        res = [[]]
        for row in range(rows):
            for col in range(cols):
                v = mat[row][col]
                if len(res[-1]) >= c:
                    res.append([v])
                else:
                    res[-1].append(v)
        return res

# Example usage:
mat1 = [[1, 2], [3, 4]]
r1, c1 = 1, 4
print(matrixReshape(mat1, r1, c1))  

mat2 = [[1, 2], [3, 4]]
r2, c2 = 2, 4
print(matrixReshape(mat2, r2, c2))  


print("==============================================================")

#Solution 2:
def matrixReshape(mat, r, c):
    # Get the dimensions of the original matrix
    m = len(mat)
    n = len(mat[0])
    
    # Check if the reshape operation is possible
    if m * n != r * c:
        return mat
    
    # Initialize an empty reshaped matrix
    reshaped = [[0 for _ in range(c)] for _ in range(r)]
    
    # Initialize indices for the reshaped matrix
    i = 0
    j = 0
    
    # Iterate over the original matrix in row-major order
    for row in mat:
        for element in row:
            # Place the current element in the reshaped matrix
            reshaped[i][j] = element
            
            # Move to the next position in the reshaped matrix
            j += 1
            if j == c:
                j = 0
                i += 1
    
    return reshaped

# Example usage:
mat1 = [[1, 2], [3, 4]]
r1, c1 = 1, 4
print(matrixReshape(mat1, r1, c1))  

mat2 = [[1, 2], [3, 4]]
r2, c2 = 2, 4
print(matrixReshape(mat2, r2, c2))  



"""# Explanation of the code:

1.  The function `matrixReshape` checks if the product of `m` and `n` (the dimensions of the original matrix) 
        is equal to the product of `r` and `c` (the dimensions of the reshaped matrix).

2.  If the products are not equal, the function returns the original matrix `mat`.
3.  If the products are equal, the function initializes an empty reshaped matrix `reshaped` with dimensions `r x c`.
4.  It then iterates over the original matrix `mat` in row-major order using nested for loops.

5.  Inside the loops, it places each element from the original matrix `mat` into the corresponding position 
        in the reshaped matrix `reshaped`, using the indices `i` and `j` to keep track of the current position.

6.  The function updates the indices `i` and `j` after placing each element, moving to the next row if necessary.
7.  Finally, the function returns the reshaped matrix `reshaped`."""








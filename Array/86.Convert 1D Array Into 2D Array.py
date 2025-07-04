#Problem
#https://leetcode.com/problems/convert-1d-array-into-2d-array/description/?envType=problem-list-v2&envId=array
" m rows "
"n columns"



#Solution 1:

def convert_to_2d_array(original, m, n):
    # Check if the total number of elements in the original array matches m * n
    if len(original) != m * n:
        return []
    
    # Initialize the 2D array
    result = []
    
    # Iterate over the original array and construct the 2D array
    for i in range(m):
        # Calculate the start and end indices for the current row
        start = i * n
        end = start + n
        # Append the current row to the result
        result.append(original[start:end])
    
    return result

# Example usage:
original1 = [1, 2, 3, 4]
m1, n1 = 2, 2
print(convert_to_2d_array(original1, m1, n1))  

original2 = [1, 2, 3]
m2, n2 = 1, 3
print(convert_to_2d_array(original2, m2, n2))  

original3 = [1, 2]
m3, n3 = 1, 1
print(convert_to_2d_array(original3, m3, n3))  


print("========================================================")

#Solution 2:
def construct2DArray(original, m, n):

    # Check if the number of elements in the 1D array is equal to m * n
    if len(original) != m * n:
        return []
    
    # Initialize an empty 2D array
    result = []
    
    # Iterate over the 1D array in steps of n
    for i in range(0, len(original), n):
        # Append a slice of n elements to the 2D array
        result.append(original[i:i+n])
    
    return result

# Example usage:
original1 = [1, 2, 3, 4]
m1, n1 = 2, 2
print(convert_to_2d_array(original1, m1, n1))  

original2 = [1, 2, 3]
m2, n2 = 1, 3
print(convert_to_2d_array(original2, m2, n2))  

original3 = [1, 2]
m3, n3 = 1, 1
print(convert_to_2d_array(original3, m3, n3))  





#Explanation : https://chat.deepseek.com/a/chat/s/8c2aa26b-e8d8-4f75-9735-6214b456623f

"""# Time and Space Complexity:
*Time complexity: O(m * n), where m is the number of rows and n is the number of columns, 
because the function iterates over all elements in the `original` array."""

#Problem : 
# https://www.youtube.com/watch?v=dwjr-7wVdaY
# https://leetcode.ca/2019-01-06-1133-Largest-Unique-Number/





#Solution 1:
def largest_unique_number(A):
    # Create a dictionary to count the occurrence of each integer
    count_dict = {}
    for num in A:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Find the largest integer that occurs only once
    max_unique = -1
    for num, count in count_dict.items():
        if count == 1 and num > max_unique:
            max_unique = num

    return max_unique


# Example usage:
A = [5, 7, 3, 9, 4, 9, 8, 3, 1]
print(largest_unique_number(A))  

A = [9, 9, 8, 8]
print(largest_unique_number(A))  



print("=====================================================")

#Solution 2:
def largest_unique_number(A):
    from collections import Counter

    # Count the occurrences of each number
    count = Counter(A)
    
    # Filter the numbers that occur only once
    unique_numbers = [num for num, freq in count.items() if freq == 1]
    
    # Return the maximum of unique numbers, or -1 if there are none
    return max(unique_numbers) if unique_numbers else -1

# Example 1
print(largest_unique_number([5,7,3,9,4,9,8,3,1]))  

# Example 2
print(largest_unique_number([9,9,8,8]))  




print("=====================================================")

#Solution 3:
def largest_unique_number(A):

    # Create a dictionary to count the occurrence of each integer
    count_dict = {}
    for num in A:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Find the largest integer that occurs only once
    max_unique = max([num for num, count in count_dict.items() if count == 1], default=-1)
    return max_unique


# Example usage:
A = [5, 7, 3, 9, 4, 9, 8, 3, 1]
print(largest_unique_number(A))  

A = [9, 9, 8, 8]
print(largest_unique_number(A))  


#Explanation : https://chatgpt.com/c/6790e8f0-fbd8-800f-80b6-43b93d524748
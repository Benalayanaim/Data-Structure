#Problem : https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/?envType=problem-list-v2&envId=stack





#Solution 1:
def finalPrices(prices):
        # Create a copy of original prices array to store discounted prices
        result = prices.copy()
        #result = prices[:]

        for i in range(len(prices)):
            # Look for first smaller or equal price that comes after current item
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    # Apply discount by subtracting prices[j] from current price
                    result[i] = prices[i] - prices[j]
                    #if we find the minimum index such that j > i stop the looping for i = 0
                    "use the complier to understand what I mean "
                    break    

        return result

prices = [8,4,6,2,3]
prices1 = [1,2,3,4,5]

print(finalPrices(prices))
print(finalPrices(prices1))
"""Explanation :
Algorithm
Initialize a variable n to store the length of the input prices array.
Initialize a result array by creating a copy of the input prices array. This ensures we have a copy of the original prices to work with.
Start an outer loop that iterates from 0 to n - 1, with loop variable i:
        Start an inner loop that iterates from index i + 1 to n - 1, with loop variable j.
            If prices[j] is less than or equal to prices[i]:
                Calculate the discounted price by subtracting prices[j] from prices[i].
                Store the calculated discounted price in result[i].
                Break the inner loop as we have found the first valid discount.
Return the result array containing all final prices after discounts."""



print("===================================")
#Solution 2:

from collections import deque 
def finalPrices(prices):
 # Create a copy of prices array to store discounted prices
        result = prices.copy()

        stack = deque()

        for i in range(len(prices)):
            # Process items that can be discounted by current price
            while stack and prices[stack[-1]] >= prices[i]:
                # Apply discount to previous item using current price
                result[stack.pop()] -= prices[i]
            # Add current index to stack
            stack.append(i)

        return result

prices = [8,4,6,2,3]
prices1 = [1,2,3,4,5]

print(finalPrices(prices))
print(finalPrices(prices1))

"""Explanation
Algorithm
Initialize:
    a result array by creating a copy of the input prices array to store the discounted prices.
    an empty stack that will store indices of prices.
For each index i of the prices array:
    Start a while loop that continues as long as:
        The stack is not empty, AND
        The price at the index stored at the stack's top is greater than or equal to the current price
        Inside the while loop, pop the top index from the stack.
        Calculate the discounted price by subtracting the current price from the price at the popped index.
        Store the result in the result array at the popped index.
    Add the current index i to the stack.
Return the result array containing all final prices after discounts."""





print("=============================================")
#Solution 3:


def finalPrices(prices):
    stack = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[i]:
            top_index = stack.pop()
            prices[top_index] -= prices[i]
        stack.append(i)
    return prices

prices = [8,4,6,2,3]
prices1 = [1,2,3,4,5]

print(finalPrices(prices))
print(finalPrices(prices1))


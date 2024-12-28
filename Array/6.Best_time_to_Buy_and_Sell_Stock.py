#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/




def maxProfit(prices):
    min_price = float('inf')  # Start with a very high minimum price
    max_profit = 0  # Initialize max profit to 0
    
    for price in prices:
        if price < min_price:
            min_price = price  # Update the minimum price
        else:
            profit = price - min_price  # Calculate profit
            if profit > max_profit:
                max_profit = profit  # Update the max profit
    
    return max_profit


prices1 = [7,1,5,3,6,4]

prices2 = [7,6,4,3,1]

print(maxProfit(prices1))
print(maxProfit(prices2))


#Another solution : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/1735550/python-javascript-easy-solution-with-very-clear-explanation/

#https://chatgpt.com/c/674cf72f-d06c-8007-b280-d0c5ab0f08ef
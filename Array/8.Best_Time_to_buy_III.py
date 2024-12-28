#Descrition 
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/



#Explanation on details about all solution here: https://chatgpt.com/c/674e3bd2-743c-8007-bbc6-2cf71797b0c3
"read one and two time the explanation and the step - you see i explain some tow time so scroll in all the page"



#Solution 1 :
def maxProfit(prices):
    if not prices:
        return 0
    
    # Initialize variables to track the two transactions
    first_buy = float('inf')  # Minimum price for first buy
    first_sell = 0            # Maximum profit after first sell
    second_buy = float('inf') # Minimum effective price for second buy
    second_sell = 0           # Maximum profit after second sell
    
    for price in prices:
        # Update the variables in order
        first_buy = min(first_buy, price)                          # Buy at the lowest price for the first transaction
        first_sell = max(first_sell, price - first_buy)            # Max profit after selling the first stock
        second_buy = min(second_buy, price - first_sell)           # Buy again with effective price reduced by first profit
        second_sell = max(second_sell, price - second_buy)         # Max profit after selling the second stock
    
    return second_sell  # Maximum profit after at most two transactions

prices = [3,3,5,0,0,3,1,4]
prices1 = [1,2,3,4,5]
prices2 = [0,4,1,6,1,9]
print(maxProfit(prices))
print(maxProfit(prices1))
print(maxProfit(prices2))




print("====================================")

#Solution 2:
def maxProfit(prices):
    if not prices or len(prices) < 2:
        return 0
    
    n = len(prices)
    
    # Step 1: Forward pass for max profit up to each day
    max_profit_up_to = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])  # Update the minimum price
        max_profit_up_to[i] = max(max_profit_up_to[i - 1], prices[i] - min_price)
    
    # Step 2: Backward pass for max profit from each day
    max_profit_from = [0] * n
    max_price = prices[-1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])  # Update the maximum price
        max_profit_from[i] = max(max_profit_from[i + 1], max_price - prices[i])
    
    # Step 3: Combine results for maximum total profit
    max_total_profit = 0
    for i in range(n):
        max_total_profit = max(max_total_profit, max_profit_up_to[i] + max_profit_from[i])
    
    return max_total_profit
prices = [3,3,5,0,0,3,1,4]
prices1 = [1,2,3,4,5]
prices2 = [0,4,1,6,1,9]
print(maxProfit(prices))
print(maxProfit(prices1))
print(maxProfit(prices2))


print("====================================")


#Solution 3

def maxProfit(prices)-> int:
    

    if len(prices) == 0:
        return 0

    buyPrice1 = float('inf')
    profit1   = float('-inf')
    buyPrice2 = float('inf')
    profit2  = float('-inf')

    
    for i in range(0,len(prices)):
        #first Transaction
        buyPrice1   = min(buyPrice1, prices[i])
        profit1     = max(profit1, prices[i] - buyPrice1)

        #Second Transaction
        buyPrice2   = min(buyPrice2, prices[i] - profit1) 
        profit2     = max(profit2, prices[i] - buyPrice2)
    

    return profit2

prices = [3,3,5,0,0,3,1,4]
prices1 = [1,2,3,4,5]
prices2 = [0,4,1,6,1,9]
print(maxProfit(prices))
print(maxProfit(prices1))
print(maxProfit(prices2))

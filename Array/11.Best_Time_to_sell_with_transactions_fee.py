#Leetcode #714 Best Time to Buy and Sell Stock with Transaction Fee

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/



def maxProfit(prices, fee):
    if not prices:
        return 0

    buy = prices[0]  # Initial cost to buy
    profit = 0       # Total profit

    for price in prices[1:]:
        # If selling is profitable, sell the stock
        if price > buy + fee:
            profit += price - buy - fee  # Sell the stock
            buy = price - fee  # Update buy to reflect "holding" this stock after selling
        
        # Update the minimum effective cost of buying
        elif price < buy:
            buy = price  # Update buy to the lower price

    return profit


prices = [1,3,2,8,4,9] 
fee = 2

prices1 = [1,3,7,5,10,3]
fee1 = 3

print(maxProfit(prices, fee))
print(maxProfit(prices1, fee1))



print("=============================")


def maxProfit(prices, fee) -> int:
    buy = float('-inf')
    sell = 0

    for price in prices:
        buy = max(buy, sell - price)
        sell = max(sell, buy + price - fee)

    return sell
prices = [1,3,2,8,4,9] 
fee = 2

prices1 = [1,3,7,5,10,3]
fee1 = 3

print(maxProfit(prices, fee))
print(maxProfit(prices1, fee1))



"#Explanation : "
# https://chatgpt.com/c/6750db73-cda0-8007-9ab5-c8c2aff10e07

#Leetcode #309 Best Time to Buy and Sell Stock with Cooldown

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/




#Solution 1 :

def maxProfit(prices):
    if not prices:
        return 0
    
    n = len(prices)
    hold = [-float('inf')] * n
    cool = [0] * n
    free = [0] * n
    
    # Base case
    hold[0] = -prices[0]
    cool[0] = 0
    free[0] = 0
    
    for i in range(1, n):
        hold[i] = max(hold[i-1], free[i-1] - prices[i])
        cool[i] = hold[i-1] + prices[i]
        free[i] = max(free[i-1], cool[i-1])
    
    # Maximum profit will be in the cool or free state
    return max(cool[-1], free[-1])

# Example usage
prices0 = [1, 2, 3, 0, 2]
prices1 = [1]

prices2 = [1,8,0,2,9]
prices3 = [1,2,0,2,9]

print(maxProfit(prices0))
print(maxProfit(prices1))
print(maxProfit(prices2))
print(maxProfit(prices3))
#A good explanation
"""
        We have three states:
            - free: starting state, no stock, can rest or buy
            - hold: just bought stock, can rest or sell
            - cool: just sold stock, must rest
        
        The reason state cool exists is that we want to force a rest between leaving hold (previous sell) and free (next buy).
        
        Each state has the following actions:
            - free:
                - free -> free: no stock, rest
                - free -> hold: buy new stock
            - hold:
                - hold -> hold: hold stock, rest
                - hold -> cool: sell stock
            - cool:
                - cool -> free: forced rest
            
        Let sk[j], k = {0, 1, 2}, j = {0, 1, ..., n}, denote the profit at state sk on day j
        (e.g., hold[2] is the profit on day 2 if we happened to be there).
        
        We have the following ways to enter each state:
            - Entering free[i]:
                - From free[i-1]: rest on day i, so profit remains the same as free[i-1]
                - From cool[i-1]: forced rest on day i, so profit remains the same as cool[i-1]
            - Entering hold[i]:
                - From hold[i-1]: rest on day i, so profit remains the same as hold[i-1]
                - From free[i-1]: bought stocks on day i, so profit is updated to (free[i-1]-profits[i])
            - Entering cool[i]:
                - From hold[i-1]: sold stock on day i, so profit is updated to (hold[i-1]+profits[i])
            
        Initial states:
            - free[0] = 0: you start with 0 profit on day 0
            - hold[0] = -prices[0]: if you bought stock on day 0, ur profit is -prices[0] 
            - cool[0] = X: dummy state as you need two days to buy and sel
"""


print("==================================")




#Solution 2 
def maxProfit(prices):
        
		# initialization
        cool_down = 0 
        sell = 0
        hold = -float('inf')
        
        for stock_price_of_Day_i in prices:
            
            prev_cool_down = cool_down 
            prev_sell = sell
            prev_hold = hold

            # Max profit of cooldown on Day i comes from either cool down of Day_i-1, 
            # or sell out of Day_i-1 and today Day_i is cooling day
            cool_down = max(prev_cool_down, prev_sell)
            
            # Max profit of sell on Day_i comes from hold of Day_i-1 and sell on Day_i
            sell = prev_hold + stock_price_of_Day_i
            
            # Max profit of hold on Day_i comes from either hold of Day_i-1, 
            # or cool down on Day_i-1 and buy on Day_i
            hold = max(prev_hold, prev_cool_down - stock_price_of_Day_i)
        
        
        # The action of final trading day must be either sell or cool down
        return max(sell, cool_down)


# Example usage
prices0 = [1, 2, 3, 0, 2]
prices1 = [1]

prices2 = [1,8,0,2,9]
prices3 = [1,2,0,2,9]

print(maxProfit(prices0))
print(maxProfit(prices1))

print(maxProfit(prices2))
print(maxProfit(prices3))



"""Explanatiojn

cool_down denotes the max profit of current Day_i, with either do nothing, or just sell out on previous day and enter cooling on Day_i

sell denotes the max profit of current Day_i, with selling stock with price quote of Day_i

hold denotes the max profit of current Day_i, with keep holding or buy and hold on Day_i
"""


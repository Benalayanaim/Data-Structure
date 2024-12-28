#Leetcode #188 Best Time to Buy and Sell Stock IV
"https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/"



#Solution 1:
def maxProfit(k, prices):
    n = len(prices)
    if n == 0 or k == 0:
        return 0
    
    # If k >= n//2, it's equivalent to unlimited transactions
    if k >= n // 2:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))
    
    # DP table
    dp = [[0] * n for _ in range(k+1)]
    
    for i in range(1, k+1):
        maxDiff = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j-1], prices[j] + maxDiff)
            maxDiff = max(maxDiff, dp[i-1][j] - prices[j])
    
    return dp[k][n-1]
# Test Case 1
k = 2
prices = [2, 4, 1]
print(maxProfit(k, prices))  # Output: 2

# Test Case 2
k = 2
prices = [3, 2, 6, 5, 0, 3]
print(maxProfit(k, prices))  # Output: 7


print("=====================")


#Solution 2:

def maxProfit(k: int, prices: int) -> int:
        n = len(prices)

        if n == 0 or k == 0:
            return 0

        # Initialize arrays to track the maximum profit after each transaction
        buyPrice = [float('inf')] * k
        profit = [float('-inf')] * k

        for price in prices:

            # Loop is needed for dealing with k transactions.

            for i in range(k):
                # Update buy[i] and profit[i] for each transaction

                buyPrice[i] = min(buyPrice[i], price - (profit[i - 1] if i > 0 else 0))
                profit[i] = max(profit[i], price - buyPrice[i])

        return profit[k - 1]
k = 2
prices = [2, 4, 1]
print(maxProfit(k, prices))  # Output: 2

# Test Case 2
k = 2
prices = [3, 2, 6, 5, 0, 3]
print(maxProfit(k, prices))  # Output: 7


print("=====================")

#Solution 3:

def maxProfit(k, prices) -> int:
        # no transaction, no profit
        if k == 0: return 0
        # dp[k][0] = min cost you need to spend at most k transactions
        # dp[k][1] = max profit you can achieve at most k transactions
        dp = [[1000, 0] for _ in range(k + 1)]
        for price in prices:
            for i in range(1, k + 1):
                # price - dp[i - 1][1] is how much you need to spend
                # i.e use the profit you earned from previous transaction to buy the stock
                # we want to minimize it
                dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
                # price - dp[i][0] is how much you can achieve from previous min cost
                # we want to maximize it
                dp[i][1] = max(dp[i][1], price - dp[i][0])
        # return max profit at most k transactions
		# or you can write `return dp[-1][1]`
        return dp[k][1]

# Test Case 1
k = 2
prices = [2, 4, 1]
print(maxProfit(k, prices))  # Output: 2

# Test Case 2
k = 2
prices = [3, 2, 6, 5, 0, 3]
print(maxProfit(k, prices))  # Output: 7


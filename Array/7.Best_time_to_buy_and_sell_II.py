

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/







#Solution
def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        # If the price is increasing, add the difference to the profit
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit

# Examples
print(maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 7
print(maxProfit([1, 2, 3, 4, 5]))      # Output: 4
print(maxProfit([7, 6, 4, 3, 1]))      # Output: 0






print("========================")


#mplementation based on container and summation function:
#Solution 2:

def maxProfit(prices):
    price_gain = []

    for idx in range(len(prices) - 1):
        if prices[idx] < prices[idx+1]:
            price_gain.append(prices[idx+1] - prices[idx])


    return sum(price_gain)

prices = [7, 1, 5, 3, 6, 4]
prices1 = [1,8,4,6,3] 
prices2 = [5,4,3,2,1]

print(maxProfit(prices))
print(maxProfit(prices1))
print(maxProfit(prices2))



#Another solution ; https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solutions/4836121/simple-beginner-friendly-dry-run-greedy-approach-readable-sol-time-o-n-space-o-1-gits/

#Explanation : https://chatgpt.com/c/674ddf3f-a83c-8007-b42b-6d4dd12b834d
# Best Time to Buy and Sell Stock

# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in 
# the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any 
# transactions, in which case the profit would be 0.

# Example 1:
    
#     Input: prices = [10,1,5,6,7,1]
#     Output: 6
    
# Example 2:
    
#     Input: prices = [10,8,7,5,2]
#     Output: 0

# calculate the minimum to calculate the buying price.
# Then selling price should be maximum.
# Then every part should be the selling, price[i] is called as selling price 
# calculate the maxprofit and then return the maxprofit:


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

         n = len(prices)
         bestbuy = prices[0]
         maxprofit = 0

         for i in range(1, n):

            if prices[i] > bestbuy:
                maxprofit = max(maxprofit, prices[i] - bestbuy)

            bestbuy = min(bestbuy, prices[i])

         return maxprofit
     

# Time complexity = O(n)
# Space complexity = O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        min_price = prices[0]
        max_profit = 0
        while i < len(prices):
            profit = prices[i] - min_price
            min_price = min(min_price,prices[i])
            max_profit = max(max_profit,profit)
            i+=1
        return max_profit
            
        
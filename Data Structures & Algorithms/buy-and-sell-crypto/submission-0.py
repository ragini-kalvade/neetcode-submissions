class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        max_profit = 0
        while i < len(prices):
            x = i-1
            while x>=0:
                profit = prices[i]-prices[x]
                max_profit = max(max_profit,profit)
                x-=1
            i+=1
        return max_profit
            
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        profit = 0
        max_profit = 0
        
        for data in prices[1:]:
            profit = max(profit + data - prev, 0)
            max_profit = max(profit, max_profit)                
            prev = data
        return max_profit

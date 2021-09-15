class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        profit = 0
        max_profit = 0
        
        for data in prices[1:]:
            diff = data - prev
            profit += diff
            if profit<0:
                profit = 0
            
            if profit > max_profit:
                max_profit = profit
                
            prev = data
        return max_profit

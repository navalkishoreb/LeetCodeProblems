from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = dict()
        total_coins = len(coins)

        def number_of_ways(current, index):
            if index >= total_coins:
                return 0
            if current > amount:
                return 0
            if current == amount:
                return 1

            if (current, index) in dp:
                return dp[current, index]

            with_coin = number_of_ways(current=current + coins[index], index=index)
            without_coin = number_of_ways(current=current, index=index + 1)
            total_ways = with_coin + without_coin
            dp[current, index] = total_ways
            return total_ways

        return number_of_ways(current=0, index=0)

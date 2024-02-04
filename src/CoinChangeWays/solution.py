from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = [0] + coins
        dp = [[0] * (len(coins)) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins))

        for index in range(1, len(coins)):
            for target in range(1, amount + 1):
                remaining = target - coins[index]
                without_coin = dp[target][index - 1]
                if remaining >= 0:
                    with_coin = dp[remaining][index]
                    total_ways = with_coin + without_coin
                    dp[target][index] = total_ways
                else:
                    dp[target][index] = without_coin

        return dp[amount][len(coins) - 1]

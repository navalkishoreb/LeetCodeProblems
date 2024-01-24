from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coins)
        dp = dict()
        dp[0] = 0
        for coin in coins:
            dp[coin] = 1

        def dfs(target_sum: int):
            if target_sum < 0:
                return -1
            if target_sum in dp:
                return dp[target_sum]

            result = [dfs(target_sum=target_sum - coin) for coin in coins]
            positive_results = [item for item in result if item > 0]
            if positive_results:
                dp[target_sum] = min(positive_results) + 1
            else:
                dp[target_sum] = -1
            return dp[target_sum]

        return dfs(target_sum=amount)

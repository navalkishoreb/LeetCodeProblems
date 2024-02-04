import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        for coin in coins:
            dp[coin] = 1

        def minimum_denominations(current, count):
            if current < 0:
                return None
            if current == 0:
                return count

            if current in dp:
                return dp[current]

            results = [
                minimum_denominations(current=current - coin, count=count + 1)
                for coin in coins
            ]
            results = [result for result in results if result]

            minimum_result = min(results) + 1 if results else None
            dp[current] = minimum_result
            return minimum_result

        result = minimum_denominations(current=amount, count=0)
        return -1 if result is None else result

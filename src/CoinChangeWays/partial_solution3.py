import copy
from collections import defaultdict
from typing import List, Dict, Set


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

            return number_of_ways(
                current=current + coins[index], index=index
            ) + number_of_ways(current=current, index=index + 1)

        return number_of_ways(current=0, index=0)

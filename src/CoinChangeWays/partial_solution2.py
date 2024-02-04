import copy
from collections import defaultdict
from typing import List, Dict, Set


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(dict)
        coins = tuple(coins)

        def number_of_ways(current, denominations):
            if current < 0:
                return 0
            if current == 0:
                return 1

            if dp.get(current, {}).get(denominations):
                return dp[current][denominations]

            total_ways = 0
            new_denominations = denominations
            for coin in denominations:
                total_ways += number_of_ways(
                    current=current - coin, denominations=new_denominations
                )
                new_denominations = list(new_denominations)
                new_denominations.remove(coin)
                new_denominations = tuple(new_denominations)
            dp[current][denominations] = total_ways
            return total_ways

        return number_of_ways(current=amount, denominations=coins)

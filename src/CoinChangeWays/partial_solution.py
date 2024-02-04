from typing import List, Dict, Set


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        class Combo:
            def __init__(self, cur=None):
                self.current = cur if cur else {coin: 0 for coin in coins}

            def __eq__(self, other):
                if isinstance(other, Combo):
                    return self.current == other.current
                return False

            def __hash__(self):
                return hash(tuple(self.current.keys()))

            def push(self, coin):
                self.current[coin] = self.current[coin] + 1

            def pop(self, coin):
                self.current[coin] = self.current[coin] - 1

            def copy(self):
                return Combo(self.current.copy())

            def __repr__(self):
                return repr(self.current)

            def __str__(self):
                return str(self.current)

        dp = dict()
        dp[0] = set()

        def number_of_ways(target: int) -> Set[Combo]:
            if target <= 0:
                return set()
            if target in dp:
                return dp[target]

            result = set()
            for coin in coins:
                ways = number_of_ways(target=target - coin)
                if ways:
                    for way in ways:
                        way_copy = way.copy()
                        way_copy.push(coin=coin)
                        result.add(way_copy)
                elif target == coin:
                    combo = Combo()
                    combo.push(coin)
                    result.add(combo)

            dp[target] = result
            return dp[target]

        return len(number_of_ways(target=amount)) if amount else 1

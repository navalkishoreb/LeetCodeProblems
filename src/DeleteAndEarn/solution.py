from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cost = {}
        for item in nums:
            if item in cost:
                cost[item] += item
            else:
                cost[item] = item
        dp = {}

        def find_max():
            if not cost:
                return 0

            key, value = cost.popitem()
            prev = cost.pop(key - 1, 0)
            next = cost.pop(key + 1, 0)
            with_key = value + find_max()
            if prev:
                cost[key - 1] = prev
            if next:
                cost[key + 1] = next
            without_key = find_max()

            result = max(with_key, without_key)
            dp[key] = result
            return result

        return find_max()

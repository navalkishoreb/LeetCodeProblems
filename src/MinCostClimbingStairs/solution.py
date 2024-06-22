from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        dp[0] = cost[0]
        dp[1] = cost[1]
        cost.append(0)
        max_cost = max(cost)

        def climb(index: int):
            if index < 0:
                return max_cost
            if index in dp:
                return dp[index]
            dp[index] = cost[index] + min(climb(index - 1), climb(index - 2))
            return dp[index]

        return climb(len(cost) - 1)

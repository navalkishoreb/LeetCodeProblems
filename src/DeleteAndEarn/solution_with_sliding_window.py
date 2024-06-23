from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        cost = [0 for _ in range(0, max_num + 1)]
        for i in nums:
            cost[i] += i

        prev_prev = 0
        prev = 0

        for value in cost:
            result = max((value + prev_prev), prev)
            prev_prev = prev
            prev = result

        return prev

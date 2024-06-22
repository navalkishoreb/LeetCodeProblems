from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def maximum_loot(index: int):
            if index in dp:
                return dp[index]
            if index + 2 >= len(nums):
                result = max(nums[index:])
                dp[index] = result
                return result
            with_index = nums[index] + maximum_loot(index + 2)
            without_index = maximum_loot(index + 1)
            result = max(with_index, without_index)
            dp[index] = result
            return result

        return maximum_loot(0)

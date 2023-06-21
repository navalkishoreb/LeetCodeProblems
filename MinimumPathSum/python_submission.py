"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200

"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0]) if m else 0
        dp = {}

        def next_element(node):
            i, j = node

            down = (i + 1, j) if i + 1 < m else None
            right = (i, j + 1) if j + 1 < n else None

            return down, right

        def dfs(node):

            if not node:
                return 0

            if node in dp:
                value = dp[node]
                # print(f"{node=!r} {value=!r}")
                return value

            down, right = next_element(node)
            down_value = dfs(down) if down else -1
            right_value = dfs(right) if right else -1

            i, j = node

            if down_value != -1 and right_value != -1:
                min_value = down_value if down_value < right_value else right_value
            elif down_value != -1:
                min_value = down_value
            elif right_value != -1:
                min_value = right_value
            else:
                min_value = 0

            value = grid[i][j] + min_value
            dp[node] = value

            # print(f"{node=!r} {value=!r}")
            return value

        return dfs((0, 0))

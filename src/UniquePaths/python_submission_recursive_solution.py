"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = {}

        def next_element(node):
            i, j = node
            down = None
            right = None
            if i+1 < m:
                down = (i+1, j)
            if j+1 < n:
                right = (i, j+1)
            return (down, right)
        
        def is_destination(node):
            i, j = node
            return i+1 == m and j+1 == n

        def dfs(node) -> int:
            if not node:
                return 0
            
            if node in dp:
                return dp[node]
            
            if is_destination(node):
                dp[node] = 1
                return 1
            
            down, right = next_element(node)
            possible_paths = dfs(down) + dfs(right)
            dp[node] = possible_paths
            return possible_paths
        
        return dfs((0,0))


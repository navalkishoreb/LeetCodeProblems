"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        dp = []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for i in range(0,m+1):
            dp.append([])
            dp[i] = [0]*(n+1)
        #print(f"{dp=!r}")
        
        for i in range(m-1,-1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    #print("obstacle")
                    dp[i][j]=0
                    continue
                if i==m-1 and j==n-1:
                    #print("destination")
                    dp[m-1][n-1] = 1
                    continue
                
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
                #print(f"{i=!r}{j=!r} {dp[i][j]=!r} {dp[i+1][j]=!r} {dp[i][j+1]=!r}")
                #print(dp)
        
        return dp[0][0]
        

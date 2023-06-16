"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.

"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        dp = {}


        def next_element(node):
            i, j = node
            down = None
            diag = None
            right = None
            if i+1 < m:
                down = (i+1,j)
            if j+1 < n:
                right = (i, j+1)
            if i+1 < m and j+1<n:
                diag = (i+1, j+1)
            
            return down, diag, right
        

        def dfs(node):
            
            if not node:
                return 0

            if node in dp:
                return dp[node]
            
            dp[node] = 0
            down, diag, right = next_element(node)
            down_square  = dfs(down)
            diag_square = dfs(diag)
            right_square = dfs(right)

            i, j = node
            if matrix[i][j] == "1":
                dp[node] = 1 + min(down_square, diag_square, right_square)
                #print(f"{node=!r} {dp[node]=!r}")
            
            return dp[node]
        
        dfs((0,0))
        #print(dp)
        return max(dp.values()) ** 2

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])
        visited_matrix = [[False for _ in range(col_count)] for _ in range(row_count)]

        number_of_islands = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= row_count or col >= col_count:
                return
            if visited_matrix[row][col]:
                return
            visited_matrix[row][col] = True
            if grid[row][col] == "1":
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        for row, row_data in enumerate(grid):
            for col, cell_value in enumerate(row_data):
                if cell_value == "1" and not visited_matrix[row][col]:
                    number_of_islands += 1
                    dfs(row, col)

        return number_of_islands

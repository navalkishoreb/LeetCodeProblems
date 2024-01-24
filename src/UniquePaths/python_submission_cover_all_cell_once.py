"""
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:


Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.


"""


from copy import copy
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m else 0

        def find_points(grid):
            source = None
            empty_cells = set()
            destination = None
            obstacles = set()
            for i, row in enumerate(grid):
                for j, col in enumerate(row):
                    if col == 1:
                        source = (i,j)
                    if col == 0:
                        empty_cells.add((i,j))
                    if col == 2:
                        destination = (i,j)
                    if col == -1:
                        obstacles.add((i,j))
            
            return source, destination, empty_cells, obstacles
        
        def next_element(node):
            i, j = node
            up = None
            down = None
            left = None
            right = None
            if i-1 >= 0:
                up = (i-1, j)
            if i+1 < m:
                down = (i+1, j)
            if j-1 >=0:
                left = (i, j-1)
            if j+1 < n:
                right = (i, j+1)
            
            return up, down, left, right

            
        source, destination, empty_cells, obstacles = find_points(grid)
        required_cells = copy(empty_cells)
        required_cells.add(source)
        #print(f"{obstacles=!r} {required_cells=!r}")
        
        def dfs(node, path):
            #print(f"{node=!r} {path=!r} {destination=!r}")
            if node in set(path):
                return 0

            if node in obstacles:
                return 0
            
            if node == destination and set(path) == required_cells:
                #print(f"Reached {path}")
                return 1
            
            if node == destination:
                return 0
            
            path.append(node)
            up, down, left, right = next_element(node)
            count_path = 0
            if up and up not in path:
                count_path += dfs(up, path)
            if down and down not in path:
                count_path += dfs(down, path)
            if left and left not in path:
                count_path += dfs(left, path)
            if right and right not in path:
                count_path += dfs(right, path)

            path.pop()
            
            #print(f"{count_path=!r}")
            return count_path
        
        return dfs(source,[])


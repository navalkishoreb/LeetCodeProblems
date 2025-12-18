class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        def convertLandToWater(r,c):
            if (r < 0
            or c < 0
            or r >= ROWS
            or c >= COLUMNS
            or grid[r][c] == 0):
                return
            
            grid[r][c] = 0
            convertLandToWater(r+1, c)
            convertLandToWater(r-1, c)
            convertLandToWater(r, c +1)
            convertLandToWater(r, c - 1)
        

        for r in range(ROWS):
            convertLandToWater(r, 0)
            convertLandToWater(r, COLUMNS-1)
        
        for c in range(COLUMNS):
            convertLandToWater(0, c)
            convertLandToWater(ROWS-1, c)
        
        enclaves = 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if (grid[r][c] == 1):
                    enclaves += 1
        
        return enclaves

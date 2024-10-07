class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        
        rows = len(grid)
        cols = len(grid[0])
        
        
        def dfs(r, c):
            
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            
            
            grid[r][c] = 'W'
            
            
            dfs(r-1, c) # up
            dfs(r+1, c) # down
            dfs(r, c-1) # left
            dfs(r, c+1) # right

        
        num_islands = 0
        
        
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == 'L':
                    dfs(r, c)
                    num_islands += 1
        
        return num_islands

solution = Solution()

# Dispatch 1
grid1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"]
]
print(solution.getTotalIsles(grid1))  

# Dispatch 2
grid2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"]
]
print(solution.getTotalIsles(grid2))  


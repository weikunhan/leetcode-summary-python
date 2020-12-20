class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        self.res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1) and not grid[i][j]:
                    self.dfs(i, j, grid)
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    self.dfs(i, j, grid)
                    self.res += 1
                    
        return self.res
    
    def dfs(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 1:
            
            return
        
        grid[row][col] = 1
        self.dfs(row + 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row - 1, col, grid)
        self.dfs(row, col - 1, grid)
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        self.res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                 if grid[i][j]:
                    self.res = max(self.res, self.dfs(i, j, grid))
                    
        return self.res
        
    def dfs(self, row, col, grid):
        temp_value = 0
        
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or not grid[row][col]:

            return temp_value
        
        grid[row][col] = 0
        temp_value += self.dfs(row + 1, col, grid)
        temp_value += self.dfs(row, col + 1, grid)
        temp_value += self.dfs(row - 1, col, grid)
        temp_value += self.dfs(row, col - 1, grid)
        temp_value += 1
        
        return temp_value
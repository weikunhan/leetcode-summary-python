class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        value_dict = set()
        self.temp_value = ''
        self.res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    self.dfs(i, j, grid)
                    value_dict.add(self.temp_value)
                    self.temp_value = ''
        
        self.res = len(value_dict)
        
        return self.res
    
    def dfs(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or not grid[row][col]:
            
            return 
        
        self.temp_value += 'o'
        grid[row][col] = 0
        self.temp_value += 'u'
        self.dfs(row + 1, col, grid)
        self.temp_value += 'd'
        self.dfs(row - 1, col, grid)
        self.temp_value += 'r'
        self.dfs(row, col + 1, grid)
        self.temp_value += 'l'
        self.dfs(row, col - 1, grid)
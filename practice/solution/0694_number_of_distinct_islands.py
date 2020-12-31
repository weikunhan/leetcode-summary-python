class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        value_dict = set()
        self.value_list = []
        self.res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    self.dfs(i, j, grid)
                    value_dict.add(''.join(self.value_list))
                    self.value_list = []
        
        self.res = len(value_dict)
        
        return self.res
    
    def dfs(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or not grid[row][col]:
            
            return 
        
        self.value_list.append('o')
        grid[row][col] = 0
        self.value_list.append('u')
        self.dfs(row + 1, col, grid)
        self.value_list.append('d')
        self.dfs(row - 1, col, grid)
        self.value_list.append('r')
        self.dfs(row, col + 1, grid)
        self.value_list.append('l')
        self.dfs(row, col - 1, grid)
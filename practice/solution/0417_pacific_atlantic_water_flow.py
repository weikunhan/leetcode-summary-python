class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        self.res = []       
        
        if not matrix: 
            
            return self.res
        
        dp_list = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            self.dfs(i, 0, -1, 1, matrix, dp_list)
            self.dfs(i, len(matrix[0]) - 1, -1, 2, matrix, dp_list)
        
        for i in range(len(matrix[0])):
            self.dfs(0, i, -1, 1, matrix, dp_list)
            self.dfs(len(matrix) - 1, i, -1, 2, matrix, dp_list)
        
        return self.res

    def dfs(self, row, col, height, state, matrix, dp_list):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] < height or (dp_list[row][col] & state == state):
            
            return
        
        dp_list[row][col] |= state
        
        if dp_list[row][col] == 3: 
            self.res.append([row, col])
        
        self.dfs(row + 1, col, matrix[row][col], dp_list[row][col], matrix, dp_list) 
        self.dfs(row - 1, col, matrix[row][col], dp_list[row][col], matrix, dp_list)
        self.dfs(row, col + 1, matrix[row][col], dp_list[row][col], matrix, dp_list)
        self.dfs(row, col - 1, matrix[row][col], dp_list[row][col], matrix, dp_list)
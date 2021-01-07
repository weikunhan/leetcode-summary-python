class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        dp_list = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        self.res = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.res = max(self.res, self.dfs(i, j, -1, matrix, dp_list))
                
        return self.res
        
    def dfs(self, row, col, target, matrix, dp_list):
        temp_value = 0
        
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] <= target:
            
            return temp_value
        
        if dp_list[row][col]:
            temp_value = dp_list[row][col]
            
            return temp_value

        temp_value = max(temp_value, self.dfs(row + 1, col, matrix[row][col], matrix, dp_list))
        temp_value = max(temp_value, self.dfs(row, col + 1, matrix[row][col], matrix, dp_list))
        temp_value = max(temp_value, self.dfs(row - 1, col, matrix[row][col], matrix, dp_list))
        temp_value = max(temp_value, self.dfs(row, col - 1, matrix[row][col], matrix, dp_list))
        temp_value += 1
        dp_list[row][col] = temp_value
        
        return temp_value
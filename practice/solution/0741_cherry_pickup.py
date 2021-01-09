class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        dp_list = [[[-sys.maxsize - 1] * (len(grid)) for _ in range(len(grid))] for _ in range(len(grid))]
        self.res = 0
        
        self.res = max(self.res, self.dfs(0, 0, 0, grid, dp_list))
        
        return self.res

    def dfs(self, a_row, a_col, b_row, grid, dp_list):
        temp_value = -1
        b_col = a_row + a_col - b_row
        
        if a_row >= len(grid) or a_col >= len(grid) or b_row >= len(grid) or b_col >= len(grid) or grid[a_row][a_col] < 0 or grid[b_row][b_col] < 0:
            
            return temp_value
        
        if a_row == len(grid) - 1 and a_col == len(grid) - 1: 
            temp_value = grid[a_row][a_col]
            
            return temp_value
        
        if dp_list[a_row][a_col][b_row] != -sys.maxsize - 1:
            temp_value = dp_list[a_row][a_col][b_row]
            
            return temp_value

        temp_value = max(temp_value, self.dfs(a_row, a_col + 1, b_row, grid, dp_list))
        temp_value = max(temp_value, self.dfs(a_row + 1, a_col, b_row + 1, grid, dp_list))
        temp_value = max(temp_value, self.dfs(a_row, a_col + 1, b_row + 1, grid, dp_list))
        temp_value = max(temp_value, self.dfs(a_row + 1, a_col, b_row, grid, dp_list))

        if temp_value < 0:
            dp_list[a_row][a_col][b_row] = temp_value
            
            return temp_value
        
        temp_value += grid[a_row][a_col]
        
        if a_row != b_row:
            temp_value += grid[b_row][b_col]
        
        dp_list[a_row][a_col][b_row] = temp_value
        
        return temp_value

#        end = len(grid)
#        dp_list = [[[-sys.maxsize - 1] * (end + 1) for _ in range(end + 1)] for _ in range(end + 1)]
#        dp_list[1][1][1] = grid[0][0]
#        res = 0
#        
#        for i in range(1, len(grid) + 1):
#            for j in range(1, len(grid) + 1):
#                for k in range(1, len(grid) + 1):
#                    l = i + j - k
#                    
#                    if dp_list[i][j][k] > 0 or l < 1 or l > len(grid) or grid[i - 1][j - 1] == -1 or grid[k - 1][l - 1] == -1:
#                        continue
#  
#                    temp_value = max(dp_list[i - 1][j][k], dp_list[i - 1][j][k - 1], dp_list[i][j - 1][k], dp_list[i][j - 1][k - 1])
#                    
#                    if temp_value < 0:
#                        continue
#                        
#                    dp_list[i][j][k] = temp_value + grid[i - 1][j - 1]
#                    
#                    if i != k:
#                        dp_list[i][j][k] += grid[k - 1][l - 1]
#                        
#                        
#        if dp_list[-1][-1][-1] > 0:
#            res = dp_list[-1][-1][-1]
#             
#        return res  
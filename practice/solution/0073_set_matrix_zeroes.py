class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        row_value_dict = set()
        col_value_dict = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    row_value_dict.add(i)
                    col_value_dict.add(j)
                    
        for key in row_value_dict:
            for i in range(len(matrix[0])):
                matrix[key][i] = 0 
                
        for key in col_value_dict:
            for i in range(len(matrix)):
                matrix[i][key] = 0 
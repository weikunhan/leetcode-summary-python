class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        row_end = len(matrix)
        row_start = 0
        col_start = 0
        col_end = 0
        res = []
        
        if not matrix:
   
            return res
    
        col_end = len(matrix[0])
    
        while row_start < row_end and col_start < col_end:
            for i in range(col_start, col_end):
                res.append(matrix[row_start][i])
                
            row_start += 1
            
            for i in range(row_start, row_end):
                res.append(matrix[i][col_end - 1])
                
            col_end -= 1
            
            if row_start < row_end:
                for i in reversed(range(col_start, col_end)):
                    res.append(matrix[row_end - 1][i])
                    
            row_end -= 1
            
            if col_start < col_end:
                for i in reversed(range(row_start, row_end)):
                    res.append(matrix[i][col_start])
                    
            col_start += 1

        return res
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        count = 1
        row_start = 0
        row_end = n
        col_start = 0
        col_end = n
        res = [[0] * n for _ in range(n)]
        
        while count <= n * n:
            for i in range(col_start, col_end):
                res[row_start][i] = count
                count += 1
                
            row_start += 1
            
            for i in range(row_start, row_end):
                res[i][col_end - 1] = count
                count += 1
                
            col_end -= 1
            
            if row_start <= row_end:
                for i in reversed(range(col_start, col_end)):
                    res[row_end - 1][i] = count
                    count += 1
                    
            row_end -= 1
                
            if col_start <= col_end:
                for i in reversed(range(row_start, row_end)):
                    res[i][col_start] = count
                    count += 1
                    
            col_start += 1
            
        return res
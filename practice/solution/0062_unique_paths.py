class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        row_end = m
        col_end = n
        dp_list = [[1] * col_end for _ in range(row_end)]
        res = 0
        
        for i in range(1, len(dp_list)):
            for j in range(1, len(dp_list[0])):
                dp_list[i][j] = dp_list[i - 1][j] + dp_list[i][j - 1]
                
        res = dp_list[-1][-1]
        
        return res
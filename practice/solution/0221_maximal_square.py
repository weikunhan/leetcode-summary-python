class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        row_end = 0
        col_end = 0
        dp_list = []
        res = 0
        
        if not matrix:
        
            return res
        
        row_end = len(matrix)
        col_end = len(matrix[0])
        dp_list= [[0] * (col_end + 1) for _ in range(row_end + 1)]
        
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                dp_list[i][j] = int(matrix[i - 1][j - 1]) + dp_list[i][j - 1] + dp_list[i - 1][j] - dp_list[i - 1][j - 1]
                
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                for k in reversed(range(min(len(matrix) - i + 1, len(matrix[0]) - j + 1) + 1)):
                    temp_value = dp_list[i + k - 1][j + k - 1] - dp_list[i + k - 1][j - 1] - dp_list[i - 1][j + k - 1] + dp_list[i - 1][j - 1]
                    
                    if temp_value == k * k:
                        res = max(res, temp_value)
                        
        return res
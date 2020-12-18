class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        row_value_set = set()
        col_value_set = set()
        res = []
        
        for row in matrix:
            row_value_set.add(min(row))
            
        for col in zip(*matrix):
            col_value_set.add(max(col))
            
        for key in row_value_set:
            if key in col_value_set:
                res.append(key)
                
        return res
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        low = 0
        high = 0
        res = False
        
        if not matrix:

            return res
        
        high = len(matrix[0]) - 1
        
        while low < len(matrix) and high >= 0:
            if matrix[low][high] == target:
                res = True
                
                return res
            elif matrix[low][high] < target:
                low += 1
            else:
                high -= 1
                
        return res
                
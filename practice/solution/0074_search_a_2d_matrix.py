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
 
        high = len(matrix) * len(matrix[0]) - 1
        
        while low <= high:
            mid = (low + high) // 2
            carry, remainder = divmod(mid, len(matrix[0]))
            
            if matrix[carry][remainder] == target:
                res = True
                
                return res
            elif matrix[carry][remainder] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return res
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        
        row_end, col_end = binaryMatrix.dimensions()
        row_start = 0
        col_start = col_end - 1
        res = -1
        
        while row_start < row_end and col_start >= 0:
            if binaryMatrix.get(row_start, col_start):
                res = col_start
                col_start -= 1
            else:
                row_start += 1
                
        return res
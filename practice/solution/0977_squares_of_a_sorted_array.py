class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        value_list = []
        res = []
        
        for num in A:
            value_list.append(num ** 2)
            
        res = sorted(value_list)
        
        return res
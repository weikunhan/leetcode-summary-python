class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        res = sorted(range(1, n + 1), key=lambda x:str(x))
        
        return res
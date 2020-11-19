class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        value_list = range(1, n + 1)
        res = []
        
        res = sorted(value_list, key=lambda x:str(x))
        
        return res
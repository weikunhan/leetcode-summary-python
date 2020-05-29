class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        
        res = cells
        carry, remainder = divmod(N, 14)
        
        if not remainder:
            remainder = 14
        
        for _ in range(remainder):
            res = [0] + [res[i - 1] ^ res[i + 1] ^ 1 for i in range(1, 7)] + [0]
            
        return res
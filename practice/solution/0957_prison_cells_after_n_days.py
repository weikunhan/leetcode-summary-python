class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        
        carry, remainder = divmod(N, 14)
        res = cells
        
        if not remainder:
            remainder = 14
            
        for _ in range(remainder):
            value_list = [0] * len(res)
                
            for i in range(1, 7):
                value_list[i] = res[i + 1] ^ res[i - 1] ^ 1
            
            res = value_list
            
        return res
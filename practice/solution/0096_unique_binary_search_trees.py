class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        end = n
        dp_list = [0] * (end + 1)
        dp_list[0] = 1
        res = 0
        
        for i in range(1, n + 1):
            for j in range(i):
                dp_list[i] += dp_list[j] * dp_list[i - j - 1]
                
        res = dp_list[-1]
        
        return res
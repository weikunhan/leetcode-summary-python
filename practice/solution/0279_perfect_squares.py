class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        end = n
        dp_list = [sys.maxsize] * (end + 1)
        dp_list[0] = 0
        res = 0
        
        for i in range(1, len(dp_list)):
            for j in range(1, int(i ** 0.5) + 1):
                dp_list[i] = min(dp_list[i], dp_list[i - j * j] + 1)
                
        res = dp_list[-1]
        
        return res
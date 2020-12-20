class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        count = abs(n)
        res = 1.0
        
        while count:
            if count % 2:
                res *= x
                
            x *= x
            count //= 2
            
        if n < 0:
            res = 1 / res
            
        return res
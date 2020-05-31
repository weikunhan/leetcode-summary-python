class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        sign = 1
        res = 0
        
        if x < 0:
            sign = -1
            x = -x
            
        while x:
            carry, remainder = divmod(x, 10)
            res = res * 10 + remainder
            x = carry
            
        res = res * sign
        
        if res > 2**31 or res < -2**31:
            res = 0
            
        return res
        
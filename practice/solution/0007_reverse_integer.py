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
            carry, reminder = divmod(x, 10)
            res = res * 10 + reminder
            x = carry
            
        res *= sign    
            
        if res > 2**31 - 1 or res < -2**31:
            res = 0
            
        return res
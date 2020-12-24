class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        target_value = x
        temp_value = 0
        res = False
        
        if x < 0:
            
            return res
        
        while x:
            carry, remainder = divmod(x, 10)
            temp_value = temp_value * 10 + remainder
            x = carry
            
        if target_value == temp_value:
            res = True
            
        return res
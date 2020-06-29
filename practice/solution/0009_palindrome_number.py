class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        temp_value = 0
        count = x
        res = False
        
        if x < 0:
            
            return res
        
        while count:
            carry, remainder = divmod(count, 10)
            temp_value = temp_value * 10 + remainder
            count = carry
            
        if x == temp_value:
            res = True
            
        return res
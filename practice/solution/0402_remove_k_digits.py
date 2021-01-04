class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        value_stack = []
        res = ''
        
        for digit in num:
            while value_stack and k > 0 and value_stack[-1] > digit:
                k -= 1
                value_stack.pop()
                
            value_stack.append(digit)
        
        while k:
            value_stack.pop()
            k -= 1
            
        res = ''.join(value_stack).lstrip('0')
        
        if not res:
            res = '0'
        
        return res
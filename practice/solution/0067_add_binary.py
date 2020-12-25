class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        carry = 0
        left = len(a) - 1
        right = len(b) - 1
        res = ''
        
        while left >= 0 or right >= 0 or carry: 
            if left >= 0 and a[left] == '1':
                carry += 1
                
                
            if right >= 0 and b[right] == '1':
                carry += 1
                
            carry, remainder = divmod(carry, 2)
            res = str(remainder) + res
            left -= 1
            right -= 1
            
        return res
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        carry = 0
        left = len(num1) - 1
        right = len(num2) - 1
        res = ''
        
        while left >= 0 or right >= 0 or carry: 
            if left >= 0:
                carry += ord(num1[left]) - ord('0')
                left -= 1
                
            if right >= 0:
                carry += ord(num2[right]) - ord('0')
                right -= 1
                
            carry, remainder = divmod(carry, 10)
            res = str(remainder) + res
            
        return res
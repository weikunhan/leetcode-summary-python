class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        end = len(num1) + len(num2)
        dp_list = [0] * (end)
        res = ''
        
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                carry = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                carry += dp_list[i + j + 1]
                carry, remainder = divmod(carry, 10)
                dp_list[i + j] += carry
                dp_list[i + j + 1] = remainder
        
        for num in dp_list:
            res += str(num)
        
        res = res.lstrip('0')
        
        if not res:
            res = '0'
            
        return res
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        sign = 1
        count = 0
        res = 0
        temp_value = str.strip()
        
        if not temp_value:
            
            return res
        
        if temp_value[0] == '-':
            sign = -1
            temp_value = temp_value[1:]
        elif temp_value[0] == '+':
            temp_value = temp_value[1:]
        else:
            pass
        
        while count < len(temp_value) and temp_value[count].isdigit():
            res = res * 10 + int(temp_value[count])
            count += 1
        
        res = max(-2**31, min(sign * res, 2**31 - 1))
            
        return res
            
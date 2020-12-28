class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        value_stack = []
        sum_value = 0
        sign = 1
        res = 0
        
        for char in s:
            if char.isdigit():
                sum_value = sum_value * 10 + int(char)
                
            if char in '+-()':
                if char == '+':
                    res += sign * sum_value
                    sign = 1
                elif char =='-':
                    res += sign * sum_value
                    sign = -1
                elif char == '(':
                    value_stack.append((res, sign))
                    sign = 1
                    res = 0
                elif char == ')':
                    res += sign * sum_value
                    temp_value, exp_value = value_stack.pop()
                    res *= exp_value
                    res += temp_value
                    
                sum_value = 0

        res += sign * sum_value
        
        return res
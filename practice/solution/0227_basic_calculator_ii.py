class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        value_stack = []
        sign = '+'
        sum_value = 0
        res = 0
        
        for char in s + '+':
            if char.isdigit():
                sum_value = sum_value * 10 + int(char)
            
            if char in '+-*/':
                if sign == '+':
                    value_stack.append(sum_value)
                    sign = char
                elif sign == '-':
                    value_stack.append(-sum_value)
                    sign = char
                elif sign == '*':
                    temp_value = value_stack.pop()
                    value_stack.append(temp_value * sum_value)  
                    sign = char
                else:
                    temp_value = value_stack.pop()
                    #carry, remainder = divmod(temp_value, sum_value)
                    #if carry < 0 and remainder:
                    #    carry += 1
                    #value_stack.append(carry)
                    value_stack.append(int(temp_value / float(sum_value)))
                    sign = char
                
                sum_value = 0
      
        res = sum(value_stack)
        
        return res         



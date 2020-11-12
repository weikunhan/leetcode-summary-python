class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        value_stack = []
        sum_value = 0
        sign = '+'
        res = 0
        
        for i in range(len(s)):
            if s[i].isdigit():
                sum_value = sum_value * 10 + int(s[i])
            
            if s[i] in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    value_stack.append(sum_value)
                    sign = s[i]
                    sum_value = 0
                elif sign == '-':
                    value_stack.append(-sum_value) 
                    sign = s[i]
                    sum_value = 0
                elif sign == '*':
                    temp_value = value_stack.pop()
                    value_stack.append(temp_value * sum_value)  
                    sign = s[i]
                    sum_value = 0
                elif sign == '/':
                    temp_value = value_stack.pop()
                    carry, remainder = divmod(temp_value, sum_value)

                    if carry < 0 and remainder:
                        carry += 1
  
                    value_stack.append(carry)
                    sign = s[i] 
                    sum_value = 0
                else:
                    pass
                        
        res = sum(value_stack)
        
        return res



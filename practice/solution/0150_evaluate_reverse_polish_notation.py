class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        value_stack = []
        res = 0
        
        for token in tokens:
            if not token in '+-*/':
                value_stack.append(int(token))
            else:
                first_value = value_stack.pop()
                second_value = value_stack.pop()
                
                if token == '+':
                    value_stack.append(second_value + first_value)
                elif token == '-':
                    value_stack.append(second_value - first_value)
                elif token == '*':
                    value_stack.append(second_value * first_value)
                else:
                    #carry, remainder = divmod(second_value, first_value)
                    #if carry < 0 and remainder:
                    #    carry += 1
                    #value_stack.append(carry)
                    value_stack.append(int(second_value / float(first_value)))
        
        res = value_stack.pop()
        
        return res 
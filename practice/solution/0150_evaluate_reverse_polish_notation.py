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
                right_value = value_stack.pop()
                left_value = value_stack.pop()
                
                if token == '+':
                    value_stack.append(int(right_value + left_value))
                elif token == '-':
                    value_stack.append(int(left_value - right_value))
                elif token == '*':
                    value_stack.append(int(right_value * left_value))
                else:
                    value_stack.append(int(left_value / float(right_value)))
                    
        res = value_stack.pop()
        
        return res
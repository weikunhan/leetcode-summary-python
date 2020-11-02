class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        value_stack = ['']
        res = ''
        
        for char in s:
            if char == '(':
                value_stack.append('')
            elif char == ')':
                temp_value = value_stack.pop()[::-1]
                value_stack[-1] += temp_value
            else:
                value_stack[-1] += char
                
        res = ''.join(value_stack.pop())
            
        return res
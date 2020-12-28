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
                temp_value = value_stack.pop()
                value_stack[-1] += temp_value[::-1]
            else:
                value_stack[-1] += char
                
        res = ''.join(value_stack[-1])
        
        return res
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        value_stack = []
        sum_value = 0
        pre_value = ''
        res = ''
        
        for char in s:
            if char =='[':
                value_stack.append(pre_value)
                value_stack.append(sum_value)
                pre_value = ''
                sum_value = 0
            elif char == ']':
                right_value = value_stack.pop()
                left_value = value_stack.pop()
                pre_value = left_value + pre_value * right_value
            elif char.isdigit():
                sum_value = sum_value * 10 + int(char)
            else:
                pre_value += char
            
        res = pre_value    
            
        return res
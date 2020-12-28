class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        value_stack = []
        sum_value = 0
        word_value = ''
        res = ''
        
        for char in s:
            if char == '[':
                value_stack.append((word_value, sum_value))
                word_value = ''
                sum_value = 0
            elif char == ']':
                temp_value, num_value = value_stack.pop()
                word_value = temp_value + word_value * num_value
            elif char.isdigit():
                sum_value = sum_value * 10 + int(char)
            else:
                word_value += char
                
        res = word_value
        
        return res
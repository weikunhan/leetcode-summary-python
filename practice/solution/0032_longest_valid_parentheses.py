class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        end = len(s)
        dp_list = [0] * (end + 1)
        value_stack = []
        res = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                value_stack.append(i)
            else:
                if value_stack:
                    temp_value = value_stack.pop()
                    dp_list[i + 1] = dp_list[temp_value] + i - temp_value + 1

          
        res = max(dp_list)
        
        return res
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        value_stack = []
        res = ''
        
        for char in S:
            if not value_stack:
                value_stack.append(char)
            else:
                if value_stack[-1] == char:
                    value_stack.pop()
                else:
                    value_stack.append(char)
                
        res = ''.join(value_stack)
                
        return res
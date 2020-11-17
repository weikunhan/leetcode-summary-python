class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        a_value_stack = []
        b_value_stack = []
        res = False
        
        for char in S:
            if char == '#':
                if a_value_stack:
                    a_value_stack.pop()
            else:    
                a_value_stack.append(char)
            
        for char in T:
            if char == '#':
                if b_value_stack:
                    b_value_stack.pop()
            else:    
                b_value_stack.append(char)
            
        if a_value_stack == b_value_stack:
            res = True
            
        return res
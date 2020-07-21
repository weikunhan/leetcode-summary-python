class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        value_stack = []
        value_dict = {']': '[', '}': '{', ')': '('}
        res = False
        
        for char in s:
            if not char in value_dict:
                value_stack.append(char)
            else:
                if not value_stack:
                    
                    return res
                
                temp_value = value_stack.pop()
                
                if value_dict[char] != temp_value:
                    
                    return res
                
        if not value_stack:
            res = True
            
        return res
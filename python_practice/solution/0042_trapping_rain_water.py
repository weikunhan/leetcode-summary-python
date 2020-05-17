class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        value_stack = []
        left = 0 
        right = 0
        res = 0
        
        for value in height:
            left = max(left, value)
            value_stack.append(left)
            
        for value in reversed(height):
            right = max(right, value)
            temp_value = value_stack.pop()
            res += min(temp_value, right) - value
            
        return res
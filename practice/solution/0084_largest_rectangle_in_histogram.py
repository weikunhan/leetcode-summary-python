class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        value_list = heights + [0]
        value_stack = [-1]
        res = 0
        
        for i in range(len(value_list)):
            while value_list[value_stack[-1]] > value_list[i]:
                temp_value = value_list[value_stack.pop()]
                res = max(res, temp_value * (i - value_stack[-1] - 1))
            
            value_stack.append(i)
            
        return res
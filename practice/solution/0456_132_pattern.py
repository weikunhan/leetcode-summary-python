class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        temp_value = -sys.maxsize - 1
        value_stack = []
        res = False
        
        for num in reversed(nums):
            if num < temp_value:
                res = True
                
                return res
            
            while value_stack and value_stack[-1] < num:
                temp_value = value_stack.pop()
                
            value_stack.append(num)
            
        return res
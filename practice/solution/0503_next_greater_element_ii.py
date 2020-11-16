class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        value_stack = []
        res = [-1] * len(nums)
        
        for _ in range(2):
            for i in range(len(nums)):
                while value_stack and nums[value_stack[-1]] < nums[i]:
                    temp_value = value_stack.pop()
                    res[temp_value] = nums[i]

                value_stack.append(i)
                
        return res
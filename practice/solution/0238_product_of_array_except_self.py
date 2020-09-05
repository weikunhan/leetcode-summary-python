class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        temp_value = 1
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            res[i] = temp_value
            temp_value *= nums[i]
            
        temp_value = 1    
            
        for i in reversed(range(len(nums))):
            res[i] *= temp_value
            temp_value *= nums[i]
            
        return res
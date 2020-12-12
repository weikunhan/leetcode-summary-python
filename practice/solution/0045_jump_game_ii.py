class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start_value = 0
        end_value = 0
        res = 0
        
        if len(nums) < 2:
            
            return res
        
        end_value = nums[0]
        res = 1
        
        while end_value < len(nums) - 1:
            temp_value = end_value
            res += 1
            
            for i in range(start_value, end_value + 1):
                temp_value = max(temp_value, i + nums[i])
            
            start_value = end_value
            end_value = temp_value
            
        return res
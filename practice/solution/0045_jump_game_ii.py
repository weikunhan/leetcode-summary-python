class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start = nums[0]
        end = nums[0]
        temp_value = 1
        res = 0
        
        if len(nums) < 2:
            
            return res
        
        for i in range(1, len(nums)):
            if start < i:
                temp_value += 1
                start = end
                
            end = max(end, nums[i] + i)
        
        res = temp_value
            
        return res      
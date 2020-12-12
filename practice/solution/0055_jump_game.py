class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        temp_value = 0
        res = False
        
        for i in range(len(nums)):
            if i > temp_value:
                
                return res
            
            temp_value = max(temp_value, i + nums[i])
            
        res = True
        
        return res
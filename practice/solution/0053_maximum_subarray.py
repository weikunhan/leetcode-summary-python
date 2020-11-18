class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp_list = nums
        res = 0
        
        for i in range(1, len(nums)):
            if dp_list[i - 1] > 0:
                dp_list[i] += dp_list[i - 1]
                    
        res = max(dp_list)            
        
        return res
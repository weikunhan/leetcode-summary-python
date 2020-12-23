class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp_list = nums
        res = 0
        
        if not nums:
            
            return res
        
        if len(nums) > 1:
            dp_list[1] = max(dp_list[1], dp_list[0])
        
        for i in range(2, len(nums)):
            dp_list[i] = max(dp_list[i - 1], dp_list[i] + dp_list[i - 2])
            
        res = dp_list[-1]
        
        return res
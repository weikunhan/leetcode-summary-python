class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp_list = nums
        res = 0
        
        if not dp_list:
            
            return res
        
        if len(dp_list) > 1:
            dp_list[1] = max(dp_list[0], dp_list[1])
            
        for i in range(2, len(dp_list)):
            dp_list[i] = max(dp_list[i] + dp_list[i - 2], dp_list[i - 1])
            
        res = dp_list[-1]
        
        return res
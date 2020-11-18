class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        end = len(nums)
        dp_list = [0] * end
        dp_list[0] = nums[0]
        res = 0
        
        for i in range(1, len(dp_list)):
            dp_list[i] = max(dp_list[i - 1] + nums[i], nums[i])
                    
        res = max(dp_list)            
        
        return res
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        end = len(nums)
        dp_list = [[0, 0] for _ in range(end)]
        dp_list[0][0] = nums[0]
        dp_list[0][1] = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            dp_list[i][0] = max(max(dp_list[i - 1][0] * nums[i], dp_list[i - 1][1] * nums[i]), nums[i])
            dp_list[i][1] = min(min(dp_list[i - 1][0] * nums[i], dp_list[i - 1][1] * nums[i]), nums[i])
            res = max(res, dp_list[i][0])
        
        return res
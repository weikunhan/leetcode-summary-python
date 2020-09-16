class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        value_list = sorted(nums)
        res = 0
        
        res = max(value_list[-1] * value_list[-2] * value_list[-3], value_list[0] * value_list[1] * value_list[-1])
        
        return res
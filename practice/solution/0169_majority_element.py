class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        value_list = sorted(nums)
        res = 0
        
        res = value_list[len(value_list) // 2]
        
        return res
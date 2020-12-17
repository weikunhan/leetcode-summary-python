class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = sorted(nums)[len(nums) // 2]
        
        return res
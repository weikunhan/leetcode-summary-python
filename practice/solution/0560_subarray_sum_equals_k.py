import collections

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        value_dict = collections.Counter()
        value_dict[0] = 1
        presum_value = 0
        res = 0
        
        for num in nums:
            presum_value += num
            res += value_dict[presum_value - k]
            value_dict[presum_value] += 1
            
        return res
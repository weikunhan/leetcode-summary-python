import collections

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        value_dict = collections.Counter(nums)
        res = 0
        
        for key, value in value_dict.items():
            if k and key + k in value_dict:
                res += 1
                
            if not k and value > 1:
                res += 1
                
        return res
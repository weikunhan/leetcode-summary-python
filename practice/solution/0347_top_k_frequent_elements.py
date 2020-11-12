import collections
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        value_dict = collections.Counter(nums)
        res = []
        
        res = heapq.nlargest(k, value_dict, key=lambda x:value_dict[x])
        
        return res
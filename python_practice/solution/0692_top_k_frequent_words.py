import collections
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        value_dict = collections.Counter(words)
        res = []
        
        res = heapq.nsmallest(k, value_dict, key=lambda x:(-value_dict[x], x))
        
        return res
        
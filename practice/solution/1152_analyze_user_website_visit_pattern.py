import collections
import heapq
import itertools

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        
        data_value_dict = collections.defaultdict(list)
        count_value_dict = collections.Counter()
        res = []
        
        for _, a, b in sorted(zip(timestamp, username, website)):
            data_value_dict[a].append(b)
            
        for value in data_value_dict.values():
            count_value_dict += collections.Counter(set(itertools.combinations(value, 3)))
            
        res = heapq.nsmallest(1, count_value_dict, key=lambda x:(-count_value_dict[x], x))[0]
        
        return res
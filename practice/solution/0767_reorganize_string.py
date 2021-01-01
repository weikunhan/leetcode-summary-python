import heapq
import collections

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        value_dict = collections.Counter(S)
        value_pq = []
        value_list = []
        prechar_value = ''
        precount_value = 0
        res = ''
        
        for key, value in value_dict.items():
            heapq.heappush(value_pq, (-value, key))
            
        while value_pq:
            count, char = heapq.heappop(value_pq)
            value_list.append(char)
            
            if precount_value < 0:
                heapq.heappush(value_pq, (precount_value, prechar_value))
                
            prechar_value = char
            precount_value = count + 1
            
        if len(value_list) == len(S):
            res = ''.join(value_list)
            
        return res
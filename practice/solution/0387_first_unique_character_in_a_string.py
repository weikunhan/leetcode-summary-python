import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        value_dict = collections.Counter(s)
        res = sys.maxsize
        
        for key, value in value_dict.items():
            if value == 1:
                res = min(res, s.index(key))
                
        if res == sys.maxsize:
            res = -1
                
        return res
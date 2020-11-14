class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        value_list = sorted(intervals)
        res = [value_list[0]]
        
        for value in value_list[1:]:
            if res[-1][1] >= value[0]:
                res[-1][1] = max(res[-1][1], value[1])
            else:
                res.append(value)
            
        return res
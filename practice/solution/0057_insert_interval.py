class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        left_value_list = []
        right_value_list = []
        start = newInterval[0]
        end = newInterval[1]
        res = []    
        
        for interval in intervals:
            if interval[0] > end:
                right_value_list.append(interval)
            elif interval[1] < start:
                left_value_list.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
                
        res = left_value_list + [[start, end]] + right_value_list
        
        return res
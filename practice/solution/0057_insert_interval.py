class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        left_value_list = []
        right_value_list = []
        start_value = newInterval[0]
        end_value = newInterval[1]
        res = []    
        
        for interval in intervals:
            if interval[0] > end_value:
                right_value_list.append(interval)
            elif interval[1] < start_value:
                left_value_list.append(interval)
            else:
                start_value = min(start_value, interval[0])
                end_value = max(end_value, interval[1])
                
        res = left_value_list + [[start_value, end_value]] + right_value_list
        
        return res
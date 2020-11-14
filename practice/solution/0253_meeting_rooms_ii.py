class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        value_list = []
        temp_value = 0
        res = 0
        
        for interval in intervals:
            value_list.append((interval[0], 1))
            value_list.append((interval[1], -1))
        
        for value in sorted(value_list):
            temp_value += value[1]
            res = max(res, temp_value)
            
        return res
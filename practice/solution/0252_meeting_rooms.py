class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
               
        value_list = sorted(intervals)
        res = False
        
        for i in range(1, len(value_list)):
            if value_list[i][0] < value_list[i - 1][1]:
                
                return res
            
        res = True
        
        return res
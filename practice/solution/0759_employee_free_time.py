"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        
        value_list = []
        res = []

        for employee in schedule:
            for interval in employee:
                value_list.append(interval)

        value_list = sorted(value_list, key=lambda x: x.start)
        temp_value = value_list[0]

        for interval in value_list[1:]:
            if temp_value.end >= interval.start:
                temp_value.end = max(temp_value.end, interval.end)
            else:
                res.append(Interval(temp_value.end, interval.start))
                temp_value = interval
        
        return res
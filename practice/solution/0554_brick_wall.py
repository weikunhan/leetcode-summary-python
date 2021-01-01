import collections

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        
        value_dict = collections.Counter()
        res = len(wall)
        
        for row in wall:
            temp_value = 0
            
            for brick in row[:-1]:
                temp_value += brick
                value_dict[temp_value] += 1
        
        if value_dict:
            res = len(wall) - max(value_dict.values())
        
        return res
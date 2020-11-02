import collections

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        
        value_dict = collections.Counter()
        res = 0
        
        for layer in wall:
            temp_value = 0
            
            for brick in layer[:-1]:
                temp_value += brick
                value_dict[temp_value] += 1
                
        if value_dict:
            res = len(wall) - max(value_dict.values())
        else:
            res = len(wall)
        
        return res
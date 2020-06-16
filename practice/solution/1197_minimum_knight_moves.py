import collections

class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        value_list = collections.deque([(0, 0, 0)])
        value_dict = set([(0, 0)])
        res = 0 
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                i, j, cost = value_list.popleft()
                
                if i == abs(x) and j == abs(y):
                    res = cost
                    
                    return res
                
                for a, b in [(i - 2, j - 1), (i - 2, j + 1), (i - 1, j - 2), (i - 1, j + 2), (i + 1, j - 2), (i + 1, j + 2), (i + 2, j - 1), (i + 2, j + 1)]:
                    if (a, b) not in value_dict and a >= -2 and b >= -2:
                        value_list.append((a, b, cost + 1))
                        value_dict.add((a, b))
                        
        return res
import collections

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        value_list = collections.deque([(0, 0, 1)])
        res = -1
        
        if grid[0][0] or grid[-1][-1]:
            
            return res
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                i, j, cost = value_list.popleft()
                
                if i == len(grid) - 1 and j == len(grid) - 1:
                    res = cost
                    
                    return res
                
                for a, b in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                    if 0 <= a and a < len(grid) and 0 <= b and b < len(grid[0]) and not grid[a][b]:
                        grid[a][b] = 1
                        value_list.append((a, b, cost + 1))
                        
        return res
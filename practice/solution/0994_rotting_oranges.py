import collections

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        count = 0
        value_list = collections.deque()
        res = -1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    
                if grid[i][j] == 2:
                    value_list.append((i, j))
                    
        if not count:
            res = 0
            
            return res
                    
        while value_list:
            temp_value = len(value_list)
            res += 1
            
            for _ in range(temp_value):
                i, j = value_list.popleft()
                
                for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if a >= 0 and a < len(grid) and b >= 0 and b < len(grid[0]) and grid[a][b] == 1:
                        grid[a][b] = 2
                        count -= 1
                        value_list.append((a, b))
            
        if count:
            res = -1
            
        return res
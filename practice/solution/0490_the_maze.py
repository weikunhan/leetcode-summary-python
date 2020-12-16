import collections

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
         
        value_list = collections.deque([start])
        res = False
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                i, j = value_list.popleft()
                maze[i][j] = -1
                
                if i == destination[0] and j == destination[1]:
                    res = True
                    
                    return res
                
                for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    row_end = i + a
                    col_end = j + b
                    
                    while row_end >= 0 and row_end < len(maze) and col_end >= 0 and col_end < len(maze[0]) and maze[row_end][col_end] != 1:
                        row_end += a
                        col_end += b
                        
                    row_end -= a
                    col_end -= b
                    
                    if not maze[row_end][col_end]:
                        value_list.append((row_end, col_end))

        return res
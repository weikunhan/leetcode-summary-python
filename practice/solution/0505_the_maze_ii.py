import heapq

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        
        value_dict = {(start[0], start[1]): 0}
        value_pq = []
        heapq.heappush(value_pq, (0, start[0], start[1]))
        res = -1
        
        while value_pq:
            cost, i, j = heapq.heappop(value_pq)
            
            if i == destination[0] and j == destination[1]:
                res = cost

                return res
            
            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                start = 0
                row_end = i + a
                col_end = j + b
                
                while row_end >= 0 and row_end < len(maze) and col_end >= 0 and col_end < len(maze[0]) and maze[row_end][col_end] != 1:
                    row_end += a
                    col_end += b
                    start += 1

                row_end -= a
                col_end -= b
                
                if not (row_end, col_end) in value_dict or cost + start < value_dict[(row_end, col_end)]:
                    value_dict[(row_end, col_end)] = cost + start
                    heapq.heappush(value_pq, (cost + start, row_end, col_end))
                                   
        return res
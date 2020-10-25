""" Max Of Min Altitudes

Given a matrix with r rows and c columns, find the maximum score of a path 
starting at [0, 0] and ending at [r-1, c-1]. The score of a path is the minimum 
value in that path. For example, the score of the path 8 -> 4 -> 5 -> 9 is 4.

Don't include the first or final entry. You can only move either down or right 
at any point in time.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/383669/

Time complexity: O(n + m)
Space complexity: O(n + m)

Example 1:
Input:
matrix = [[5, 1],
          [4, 5]]
Output: 
4
Explanation:
Possible paths:
5 -> 1 -> 5 => min value is 1
5 -> 4 -> 5 => min value is 4
Return the max value among minimum values => max(4, 1) = 4.

Example 2:
Input:
matrix = [[1, 2, 3],
          [4, 5, 1]]
Output: 
4
Explanation:
Possible paths:
1-> 2 -> 3 -> 1
1-> 2 -> 5 -> 1
1-> 4 -> 5 -> 1
So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
Return the max of that, so 4.
"""

import heapq
import sys

class Solution(object):
    def max_of_min_altitudes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        value_pq = []
        heapq.heappush(value_pq, (-sys.maxsize, len(matrix) - 1, len(matrix[0]) - 1))
        matrix[-1][-1] = -1
        res = sys.maxsize
        
        while value_pq:
            temp_value, i, j = heapq.heappop(value_pq)
            res = min(-temp_value, res)
            
            for a, b in [(i - 1, j), (i, j - 1)]:
                if not a and not b:
                    
                    return res
                
                if a >= 0 and a < len(matrix) and b >= 0 and b < len(matrix[0]) and matrix[a][b] != -1:
                    heapq.heappush(value_pq, (-matrix[a][b], a, b))
                    matrix[a][b] = -1

        if res == sys.maxsize:
            res = 0

        return res


def main(): 
    matrix = [[1, 2, 3],
              [4, 5, 1]]
    solution = Solution()
    res = solution.max_of_min_altitudes(matrix)
    print(res)

if __name__ == "__main__": 
    main()
""" Treasure Island II

You have a map that marks the locations of treasure islands. Some of the map 
area has jagged rocks and dangerous reefs. Other areas are safe to sail in. 
There are other explorers trying to find the treasure. So you must figure out 
a shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of 
characters. You must start from one of the starting point (marked as S) of the
map and can move one block up, down, left or right at a time. The treasure 
island is marked as X. Any block with dangerous rocks or reefs will be marked 
as D. You must not enter dangerous blocks. You cannot leave the map area. 
Other areas O are safe to sail in. Output the minimum number of steps to get 
to any of the treasure islands.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/356150

Time complexity: O((mn)^2)
Space complexity: O(mn)

Example1:
Input:
gird = [['S', 'O', 'O', 'S', 'S'],
        ['D', 'O', 'D', 'O', 'D'],
        ['O', 'O', 'O', 'O', 'X'],
        ['X', 'D', 'D', 'O', 'O'],
        ['X', 'D', 'D', 'D', 'O']]
Output:
3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) 
(3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).

Example2:
Input:
gird = [['S', 'O', 'O', 'S', 'S'],
        ['D', 'O', 'D', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'X'],
        ['X', 'D', 'D', 'O', 'O'],
        ['X', 'D', 'D', 'D', 'O']]
Output:
2
"""

import collections
import sys

class Solution(object):
    def treasure_islandII(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        res = sys.maxsize

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    res = min(res, self.helper(i, j, grid))

        return res

    def helper(self, row, col, grid):
        value_list = collections.deque([(row, col, 0)])
        visit_dict = set([(row, col)])

        while value_list:
            temp_value = len(value_list)

            for _ in range(temp_value):
                i, j, cost = value_list.popleft()

                if grid[i][j] == 'X':

                    return cost

                for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if a >= 0 and a < len(grid) and b >= 0 and b < len(grid[0]) and grid[a][b] != 'D' and not (a, b) in visit_dict:
                        visit_dict.add((a, b))
                        value_list.append((a, b, cost + 1))

        return 0

def main():
    gird = [['S', 'O', 'O', 'S', 'S'],
            ['D', 'O', 'D', 'O', 'D'],
            ['O', 'O', 'O', 'O', 'X'],
            ['X', 'D', 'D', 'O', 'O'],
            ['X', 'D', 'D', 'D', 'O']]
    solution = Solution()
    res = solution.treasure_islandII(gird)
    print(res)

if __name__ == "__main__": 
    main()
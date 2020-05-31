""" Treasure Island

You have a map that marks the location of a treasure island. Some of the map 
area has jagged rocks and dangerous reefs. Other areas are safe to sail in. 
There are other explorers trying to find the treasure. So you must figure out 
a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of 
characters. You must start from the top-left corner of the map and can move one 
block up, down, left or right at a time. The treasure island is marked as X in a 
block of the matrix. X will not be at the top-left corner. Any block with 
dangerous rocks or reefs will be marked as D. You must not enter dangerous 
blocks. You cannot leave the map area. Other areas O are safe to sail in. 
The top-left corner is always safe. Output the minimum number of steps to 
get to the treasure.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/347457

Time complexity: O(mn)
Space complexity: O(mn)

Example1:
Input:
gird = [['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['O', 'O', 'O', 'O'],
        ['X', 'D', 'D', 'O']]
Output: 
5
Explanation: 
Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.

Example2:
Input:
gird = [['O', 'O', 'O', 'X'],
        ['O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O']]
Output: 
3
"""

import collections

class Solution(object):
    def treasure_island(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        value_list = collections.deque([(0, 0, 0)])
        grid[0][0] = 'D'
        res = 0

        while value_list:
            temp_value = len(value_list)

            for _ in range(temp_value):
                i, j, cost = value_list.popleft()

                if grid[i][j] == 'X':
                    res = cost

                    return res

                for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if a >= 0 and a < len(grid) and b >= 0 and b < len(grid[0]) and grid[a][b] != 'D':
                        if grid[a][b] == 'O':
                            grid[a][b] = 'D'
                        
                        value_list.append((a, b, cost + 1))

        return res

def main():
    gird = [['O', 'O', 'O', 'X'],
            ['O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O']]
    solution = Solution()
    res = solution.treasure_island(gird)
    print(res)

if __name__ == "__main__": 
    main()
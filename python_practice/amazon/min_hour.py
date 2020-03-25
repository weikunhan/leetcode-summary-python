"""  Zombie in Matrix

Given a 2D grid, each cell is either a zombie 1 or a human 0. 
Zombies can turn adjacent (up/down/left/right) human beings into zombies 
every hour. Find out how many hours does it take to infect all humans?

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/411357/

Time complexity: O(n^2)
Space complexity: O(n^2)

Example 1:
Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]
Output: 2
Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]
At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
 """

import collections

class Solution(object):
    def min_hour(self, rows, colums, grid):
        """
        :type rows: int
        :type colums: int
        :type grid: List[List[int]]
        :rtype: int
        """

        value_list = collections.deque()
        res = -1

        if not grid:
            res = 0

            return res 

        for i in range(rows):
            for j in range(colums):
                if grid[i][j] == 1:
                    value_list.append((i, j))

        while value_list:
            temp_value = len(value_list)
            res += 1

            for _ in range(temp_value):
                i, j = value_list.popleft()

                for a, b in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if a >= 0 and a < rows and b >= 0 and b < colums and grid[a][b] != 1:
                        grid[a][b] = 1
                        value_list.append((a, b))

        return res

def main():
    gird = [[0, 1, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0]]
    rows = 4
    cols = 5
    solution = Solution()
    res = solution.min_hour(rows, cols, gird)
    print(res)

if __name__ == "__main__": 
    main()
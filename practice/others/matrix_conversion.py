""" matrix_conversion

After a noval algorithm, the int 2D matrix can be converting into another int 2D
matrix. The algorithm is like that:

before_matrix = [[1, 2], [3, 4]]
after_matrix = before_matrix

for i in range(1, len(before_matrix)):
    after_matrix[i][0] += after_matrix[i - 1][0]

for i in range(1, len(before_matrix[0])):
    after_matrix[0][i] += after_matrix[0][i - 1]

for i in range(1, len(before_matrix)):
    for j in range(1, len(before_matrix[0])):
        after_matrix[i][j] += after_matrix[i][j - 1] + after_matrix[i - 1][j] - after_matrix[i - 1][j - 1]

The every element (x, y) in the new matrix is equale to the sum of previous row
and col. Now, given you a after_matrix, could you get back the before_matrix?

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://www.1point3acres.com/bbs/thread-595086-1-1.html

Time complexity:  O(mn)
Space complexity: O(mn)

Example 1:
Input: 
[[1, 3],
 [4, 10]]
Output: 
[[1, 2],
 [3, 4]]

Example 2:
Input: 
[[1, 3, 6],
 [5, 12, 21],
 [12, 27, 45]]
Output: 
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
"""

class Solution(object):
    def matrix_conversion(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        dp_list = matrix
        row_end = 0
        col_end = 0
        res = []

        if dp_list:
            row_end = len(dp_list)
            col_end = len(dp_list[0])
        else:
            
            return res

        for i in reversed(range(1, row_end)):
            for j in reversed(range(1, col_end)):
                dp_list[i][j] = dp_list[i][j] - dp_list[i][j - 1] - dp_list[i - 1][j] + dp_list[i - 1][j - 1]

        for i in reversed(range(1, row_end)):
            dp_list[i][0] -= dp_list[i - 1][0]

        for i in reversed(range(1, col_end)):
            dp_list[0][i] -= dp_list[0][i - 1]

        res = dp_list

        return res

def main():
    matrix = [[1, 3, 6],
              [5, 12, 21],
              [12, 27, 45]]
    solution = Solution()
    res = solution.matrix_conversion(matrix)
    print(res)

if __name__ == "__main__": 
    main()

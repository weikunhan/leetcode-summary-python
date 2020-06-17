""" Grouping Options

There are a number of people in a row. They must all be divided into a number of 
contiguous groups from left to right. If each group must be at least as large 
as the group to its left, determine how many distinct ways groups can be formed.
For a group to be distinct, it must differ in size for at least one group when 
sorted ascending. For exmample, [1, 1, 1, 3] is distinct from [1, 1, 1, 2] but
not from [1, 3, 1, 1].

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://www.1point3acres.com/bbs/thread-606351-1-1.html

Time complexity: O(mn)
Space complexity: O(mn)

Example 1:
Input: 
n = 8
k = 4
Output: 
5
Explanation:
[1,1,1,5], [1,1,2,4], [1,1,3,3], [1,2,2,3], [2,2,2,2]
"""

class Solution(object):
    def grouping_options(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: inta6
        """

        row_end = n
        col_end = k
        dp_list = [[0] * (col_end + 1) for _ in range(row_end + 1)]
        dp_list[0][0] = 1
        res = 0

        for i in range(1, row_end + 1):
            for j in range(1, min(col_end, i) + 1):
                dp_list[i][j] = dp_list[i - j][j] + dp_list[i - 1][j - 1]

        return dp_list[-1][-1]

def main(): 
    n = 8
    k = 4
    solution = Solution()
    res = solution.grouping_options(n, k)
    print(res)

if __name__ == "__main__": 
    main()
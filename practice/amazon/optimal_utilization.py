""" Optimal Utilization

Given 2 lists a and b. Each element is a pair of integers where the 
first integer represents the unique id and the second integer represents a value. 
Your task is to find an element from a and an element form b such that 
the sum of their values is less or equal to target and 
as close to target as possible. Return a list of ids of selected elements. 
If no pair is possible, return an empty list.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/373202

Time complexity: O(mlogm + nlogn + max(m + n))
Space complexity: O(1)

Example 1:
Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
Output: [[2, 1]]
Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], 
which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.

Example 2:
Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10
Output: [[2, 4], [3, 2]]
Explanation:
There are two pairs possible. Element with id = 2 from the list `a` has a 
value 5, and element with id = 4 from the list `b` also has a value 5.
Combined, they add up to 10. Similarily, element with id = 3 from `a` 
has a value 7, and element with id = 2 from `b` has a value 3.
These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].

Example 3:
Input:
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20
Output: [[3, 1]]

Example 4:
Input:
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20
Output: [[1, 3], [3, 2]]

Example 5:
a = [[1, 5], [2, 5]]
b = [[1, 5], [2, 5]]
target = 10
Output: [[1, 1], [1, 2], [2, 1], [2, 2]]
"""

import sys

class Solution(object):
    def optimal_utilization(self, a, b, target):
        """
        :type a: List[List[int]]
        :type a: List[List[int]]
        :type target: int
        :rtype: List[int]
        """

        temp_value = -sys.maxsize - 1
        a_value_list = sorted(a, key=lambda x: x[1])
        b_value_list = sorted(b, key=lambda x: x[1])
        left = 0
        right = len(b_value_list) - 1
        res = []

        while left < len(a_value_list) and right >= 0:
            sum_value = a_value_list[left][1] + b_value_list[right][1]

            if sum_value > target:
                right -= 1
            else:
                if temp_value <= sum_value:
                    if temp_value < sum_value:
                        res = []
                        temp_value = sum_value
                    
                    res.append([a_value_list[left][0], b_value_list[right][0]])
                    count = right

                    while count > 0 and b_value_list[count][1] == b_value_list[count - 1][1]:
                        res.append([a_value_list[left][0], b_value_list[count - 1][0]])
                        count -= 1

                left += 1

        if not res:
            res = [[]]

        return res

def main():
    a = [[1, 5], [2, 5]]
    b = [[1, 5], [2, 5]]
    target = 10
    solution = Solution()
    res = solution.optimal_utilization(a, b, target)
    print(res)

if __name__ == "__main__": 
    main()
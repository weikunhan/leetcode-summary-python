""" Min Cost to Connect Ropes

https://leetcode.com/problems/minimum-cost-to-connect-sticks (premium)

Given n ropes of different lengths, we need to connect these ropes into one rope. 
We can connect only 2 ropes at a time. The cost required to connect 2 ropes is 
equal to sum of their lengths. The length of this connected rope is also equal 
to the sum of their lengths. This process is repeated until n ropes are connected 
into a single rope. Find the min possible cost required to connect all ropes.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/344677

Time complexity: O(nlogn)
Space complexity: O(n)

Example 1:
Input: 
ropes = [8, 4, 6, 12]
Output: 
58
Explanation: The optimal way to connect ropes is as follows
1. Connect the ropes of length 4 and 6 (cost is 10). Ropes after connecting: [8, 10, 12]
2. Connect the ropes of length 8 and 10 (cost is 18). Ropes after connecting: [18, 12]
3. Connect the ropes of length 18 and 12 (cost is 30).
Total cost to connect the ropes is 10 + 18 + 30 = 58

Example 2:
Input: 
ropes = [20, 4, 8, 2]
Output: 
54

Example 3:
Input: 
ropes = [1, 2, 5, 10, 35, 89]
Output: 
224
"""

import heapq

class Solution(object):
    def min_cost_to_conneect_ropes(self, ropes):
        """
        :type ropes: List[int]
        :rtype: int
        """

        value_pq = ropes
        heapq.heapify(value_pq)
        res = 0

        while len(value_pq) > 1:
            temp_value = heapq.heappop(value_pq) + heapq.heappop(value_pq)
            res += temp_value
            heapq.heappush(value_pq, temp_value)

        return res

def main():
    ropes = [8, 4, 6, 12]
    solution = Solution()
    res = solution.min_cost_to_conneect_ropes(ropes)
    print(res)

if __name__ == "__main__": 
    main()
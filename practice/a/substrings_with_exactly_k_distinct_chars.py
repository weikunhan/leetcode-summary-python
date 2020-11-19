""" Substrings with exactly K distinct chars

Given a string s and an int k, return an int representing the number of 
substrings (not unique) of s with exactly k distinct characters. 
If the given string doesn't have k distinct characters, return 0.
https://leetcode.com/problems/subarrays-with-k-different-integers
Constraints:
- The input string consists of only lowercase English letters [a-z]
- 0 <= k <= 26

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/370157

Time complexity: O(n)
Space complexity: O(k)

Example 1:
Input: 
s = "pqpqs"
k = 2
Output: 
7
Explanation: 
["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
Example 2:
Input: 
s = "aabab"
k = 3
Output: 
0
"""

import collections

class Solution(object):
    def substrings_with_exactly_k_distinct_chars(self, s, k):
        """
        :type s: List[string]
        :type k: int
        :rtype: int
        """

        self.res = 0

        self.res = self.helper(s, k) - self.helper(s, k - 1)

        return self.res

    def helper(self, s, max_length):
        value_dict = collections.Counter()
        right = 0
        left = 0
        count = 0

        while right < len(s):
            temp_value = s[right]
            value_dict[temp_value] += 1

            if value_dict[temp_value] == 1:
                max_length -= 1

            while max_length < 0:
                temp_value = s[left]
                value_dict[temp_value] -= 1

                if not value_dict[temp_value]:
                    max_length += 1

                left += 1
            
            count += right - left + 1
            right += 1

        return count

def main(): 
    s = "pqpqs"
    k = 2
    solution = Solution()
    res = solution.substrings_with_exactly_k_distinct_chars(s, k)
    print(res)

if __name__ == "__main__": 
    main()
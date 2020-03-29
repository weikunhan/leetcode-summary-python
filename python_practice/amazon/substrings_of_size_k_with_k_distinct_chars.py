""" Substrings of size K with K distinct chars

Given a string s and an int k, return all unique substrings of s of size k with 
k distinct characters.
Constraints:
- The input string consists of only lowercase English letters [a-z]
- 0 <= k <= 26

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/370112

Time complexity: O(n)
Space complexity: O(n)

Example 1:
Input: 
s = "abcabc"
k = 3
Output: 
["abc", "bca", "cab"]

Example 2:
Input: 
s = "abacab"
k = 3
Output: 
["bac", "cab"]
Example 3:
Input: 
s = "awaglknagawunagwkwagl"
k = 4
Output: 
["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", 
"nagw", "agwk", "kwag"]
Explanation: 
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", 
"awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" "wagl" is repeated twice, 
but is included in the output once.
"""

class Solution(object):
    def substrings_of_size_k_with_k_distinct_chars(self, s, k):
        """
        :type s: List[string]
        :type k: int
        :rtype: int
        """

        value_dict = set()
        right = 0
        left = 0
        res = set()

        while right < len(s) and left < len(s):
            if not s[right] in value_dict:
                value_dict.add(s[right])
                right += 1

                if right - left == k:
                    res.add(s[left:right])
                    value_dict.remove(s[left])
                    left += 1
            else:
                value_dict.remove(s[left])
                left += 1
        
        res = list(res)

        return res

def main(): 
    s = "awaglknagawunagwkwagl"
    k = 4
    solution = Solution()
    res = solution.substrings_of_size_k_with_k_distinct_chars(s, k)
    print(res)

if __name__ == "__main__": 
    main()
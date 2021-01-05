""" Top K Frequently Mentioned Keywords

Given a list of reviews, a list of keywords and an integer k. 
Find the most popular k keywords in order of most to least frequently mentioned.
The comparison of strings is case-insensitive. If keywords are mentioned an 
equal number of times in reviews, sort alphabetically.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/542597/

Time complexity: O(mn + klogn)
Space complexity: O(mn)

Example 1:
Input:
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]
Output:
["anacell", "betacellular"]
Explanation:
"anacell" is occuring in 2 different reviews and "betacellular" is only occuring 
in 1 review.

Example 2:
Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
Output:
["betacellular", "anacell"]
Explanation:
"betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" 
are occuring in 2 reviews, but "anacell" is lexicographically smaller.
"""

import collections
import heapq
import re

class Solution(object):
    def topKFrequentMentionedKeywords(self, keywords, reviews, k):
        """
        :type keywords: List[str]
        :type reviews: List[str]
        :type k: int
        :rtype: List[str]
        """

        count_value_dict = collections.Counter()
        data_value_dict = set(keywords)
        res = []

        for review in reviews:
            temp_list = re.split(r'[,\s]', review.lower())

            for word in temp_list:
                word = re.sub(r'[^a-z0-9]', '', word)

                if word and word in data_value_dict:
                    count_value_dict[word] += 1

        res = heapq.nsmallest(k, count_value_dict, key=lambda x: (-count_value_dict[x], x))

        return res

def main():
    k = 2
    keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
    reviews = [
      "I love anacell Best services; Best services provided by anacell",
      "betacellular has great services",
      "deltacellular provides much better services than betacellular",
      "cetracular is worse than anacell",
      "Betacellular is better than deltacellular.",
    ]
    solution = Solution()
    res = solution.topKFrequentMentionedKeywords(keywords, reviews, k)
    print(res)

if __name__ == "__main__": 
    main()
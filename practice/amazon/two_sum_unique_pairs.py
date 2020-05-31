""" Two Sum - Unique Pairs

Given an int array nums and an int target, find how many unique pairs in the 
array such that their sum is equal to target. Return the number of pairs.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/372434

Time complexity: O(n)
Space complexity: O(n)

Example 1:
Input: 
nums = [1, 1, 2, 45, 46, 46]
target = 47
Output: 
2
Explanation:
1 + 46 = 47
2 + 45 = 47

Example 2:
Input: 
nums = [1, 1]
target = 2
Output: 
1
Explanation:
1 + 1 = 2

Example 3:
Input: 
nums = [1, 5, 1, 5]
target = 6
Output: 
1
Explanation:
[1, 5] and [5, 1] are considered the same.
"""

class Solution(object):
    def two_sum_unique_pairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        visit_value_dict = set()
        target_value_dict = set()
        res = 0
        
        for num in nums:
            temp_value = target - num
            
            if not num in target_value_dict:
                target_value_dict.add(temp_value)
            else:
                visit_value_dict.add((num, temp_value))

        res = len(visit_value_dict)

        return res

def main(): 
    nums = [1, 1, 2, 45, 46, 46]
    target = 47
    solution = Solution()
    res = solution.two_sum_unique_pairs(nums, target)
    print(res)

if __name__ == "__main__": 
    main()
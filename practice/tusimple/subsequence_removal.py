""" Subsequence Removal

Remove the shortest ascending subarray in an input array. If each element in the 
left subsequence is unique and it in ascending order, then return this left 
subsequence. If cannot find such a subsequence, then return [- 1].

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://www.1point3acres.com/bbs/thread-592043-1-1.html

Time complexity:  O(n^2)
Space complexity: O(1)

Example 1:
Input: 
nums = [1, 2, 7, 8, 8, 3, 3, 3, 3]
output:
[-1]
Explanation: 
Cannot find a ascending order subarray make left subsequence have unique numbers 
wich ascending order

Example 2:
Input: 
nums = [1, 2, 7, 8, 8, 3, 4, 5, 6]
output:
[1, 2, 3, 4, 5, 6]
Explanation: 
Remove [7, 8, 8], then [1, 2, 3, 4, 5, 6] have unique numbers wich ascending order

Example 3:
Input: 
nums = [2, 3, 1, 2, 3, 4, 5, 6]
output:
[1, 2, 3, 4, 5, 6]
Explanation: 
Remove [2, 3], then [1, 2, 3, 4, 5, 6] have unique numbers wich ascending order
"""

class Solution(object):
    def subsequence_removal(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target_value_list = nums[:i] + nums[j:]
                sub_value_list = nums[i:j]

                if sorted(sub_value_list) == sub_value_list and sorted(target_value_list) == target_value_list and len(target_value_list) == len(set(target_value_list)):
                    if not res or len(res) < target_value_list:
                        res = target_value_list

        if not res:
            res = [-1]

        return res

def main(): 
    nums = [1, 2, 7, 8, 8, 3, 3, 3, 3]
    solution = Solution()
    res = solution.subsequence_removal(nums)
    print(res)

if __name__ == "__main__": 
    main()
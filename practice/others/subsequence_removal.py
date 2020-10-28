""" Subsequence Removal

Remove minmian number of elements in ascending order from an input array. 
If each element in the left subsequence is unique, then return the sampled 
subarray. If cannot find such way to sample in ascending order, then return [- 1].

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://www.1point3acres.com/bbs/thread-592043-1-1.html

Time complexity:  O(n^2)
Space complexity: O(n)

Example 1:
Input: 
nums = [1, 2, 7, 8, 8, 3, 3, 3, 3]
output:
[-1]
Explanation: 
Cannot find a ascending order subarray make left subsequence have unique numbers 

Example 2:
Input: 
nums = [1, 2, 3, 4, 5, 6]
output:
[]
Explanation: 
Don't make any sampling which left subsequence have unique numbers 

Example 3:
Input: 
nums = [1, 2, 3, 4, 5, 5, 6, 6]
output:
[5, 6]
Explanation: 
Remove [5, 6], then [1, 2, 3, 4, 5, 6] have unique numbers 

Example 4:
Input: 
nums = [1, 5, 2, 3, 4, 5, 6]
output:
[5]
Explanation: 
Remove [5], then [1, 2, 3, 4, 5, 6] have unique numbers 

Example 4:
Input: 
nums = [1, 5, 2, 6, 3, 7, 4, 5, 6]
output:
[5, 6]
Explanation: 
Remove [5, 6], then [1, 2, 3, 7, 4, 5, 6] have unique numbers 
"""

import collections

class Solution(object):
    def subsequence_removal(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        value_list = []

        if len(nums) == len(set(nums)):
            
            return res
        
        for i in range(len(nums)):
            sub_value_list = []
            target_value_list = nums[:i]

            for j in range(i, len(nums)):
                temp_list = []

                if i == j:
                    sub_value_list.append(nums[j])
                    temp_list = target_value_list + nums[j + 1:]
                else:
                    if nums[j] < sub_value_list[-1]:
                        target_value_list.append(nums[j])
                    else:
                        sub_value_list.append(nums[j])

                    temp_list = target_value_list + nums[j + 1:]
                
                if len(temp_list) == len(set(temp_list)):
                    if not value_list or len(value_list) < len(temp_list):
                        value_list = temp_list
            
        if value_list:
            res = list(collections.Counter(nums) - collections.Counter(value_list))

        if not res:
            res = [-1]

        return res

def main(): 
    nums = [1, 2, 3, 4, 5, 6]
    solution = Solution()
    res = solution.subsequence_removal(nums)
    print(res)

if __name__ == "__main__": 
    main()
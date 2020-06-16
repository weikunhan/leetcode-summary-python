""" Subsequence Removal II

Remove minmian number of elements in ascending order from an input array. 
If each element in the left subsequence is unique and it in ascending order, 
then return this left subsequence. If cannot find such a subsequence, 
then return [-1].

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://www.1point3acres.com/bbs/thread-592043-1-1.html

Time complexity:  O(n^2logn)
Space complexity: O(n)

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

Example 4:
Input: 
nums = [2, 3, 2]
output:
[2, 3]
Explanation: 
Remove [2], then [2, 3] have unique numbers wich ascending order

Example 5:
Input: 
nums = [1, 2, 3]
output:
[]
Explanation: 
Remove [], then [1, 2, 3] have unique numbers wich ascending order

Example 6:
Input: 
nums = [2, 1, 3, 2, 4, 4, 5, 6]
output:
[1, 2, 4, 5, 6]
Explanation: 
Remove [2] + [3] + [4], then [1, 2, 4, 5, 6] have unique numbers wich ascending order
"""

class Solution(object):
    def subsequence_removal_ii(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []

        if sorted(nums) == nums and len(nums) == len(set(nums)):
            
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
                
                if sorted(temp_list) == temp_list and len(temp_list) == len(set(temp_list)):
                    if not res or len(res) < len(temp_list):
                        res = temp_list
                        
        if not res:
            res = [-1]

        return res

def main(): 
    nums = [1, 2, 7, 8, 8, 3, 3, 3, 3]
    solution = Solution()
    res = solution.subsequence_removal_ii(nums)
    print(res)

if __name__ == "__main__": 
    main()
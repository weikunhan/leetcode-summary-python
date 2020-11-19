""" Find Pair With Given Sum

Given a list of positive integers nums and an int target, return indices of the 
two numbers such that they add up to a target - 30.
Conditions:
- You will pick exactly 2 numbers.
- You cannot pick the same element twice.
- If you have muliple pairs, select the pair with the largest number.

Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://leetcode.com/discuss/interview-question/356960

Time complexity: O(n)
Space complexity: O(n)

Example 1:
Input: 
nums = [1, 10, 25, 35, 60]
target = 90
Output: 
[2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30

Example 2:
Input: 
nums = [20, 50, 40, 25, 30, 10]
target = 90
Output: 
[1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number.

Example 3:
Input: 
nums = [0, 0]
target = 30
Output: 
[0, 1]
"""

class Solution(object):
    def find_pair_with_given_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        target -= 30
        value_dict = {}
        max_value = -1
        res = [-1, -1]
        
        for i in range(len(nums)):
            temp_value = target - nums[i]
            
            if not nums[i] in value_dict:
                value_dict[temp_value] = i
            else:
                if nums[i] > max_value or temp_value > max_value:
                    res[0] = value_dict[nums[i]]
                    res[1] = i
                    max_value = temp_value
        
        return res

def main(): 
    nums = [1, 10, 25, 35, 60]
    target = 90
    solution = Solution()
    res = solution.find_pair_with_given_sum(nums, target)
    print(res)

if __name__ == "__main__": 
    main()
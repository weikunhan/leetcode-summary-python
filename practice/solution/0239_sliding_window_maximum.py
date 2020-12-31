import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        value_list = collections.deque()
        res = []
        
        for i in range(len(nums)):
            if value_list and i - value_list[0] == k:
                value_list.popleft()
                
            while value_list and nums[value_list[-1]] < nums[i]:
                value_list.pop()
                
            value_list.append(i)
            
            if i - k + 1 >= 0:
                res.append(nums[value_list[0]])
                
        return res
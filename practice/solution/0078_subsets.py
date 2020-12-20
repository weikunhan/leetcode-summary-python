class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        self.res = []
        
        self.dfs(0, nums, [])
        
        return self.res
    
    def dfs(self, start, nums, value_list):
        self.res.append(value_list)
        
        for i in range(start, len(nums)):
            self.dfs(i + 1, nums, value_list + [nums[i]])
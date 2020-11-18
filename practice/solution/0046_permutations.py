class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        self.res = []
        
        self.dfs(nums, [])
        
        return self.res
    
    def dfs(self, nums, value_list):
        if not nums:
            self.res.append(value_list)
            
            return
            
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], value_list + [nums[i]])
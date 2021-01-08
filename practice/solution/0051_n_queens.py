class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        self.temp_value = '.' * n
        self.res = []
        self.dfs(0, [-1] * n, [])
        
        return self.res
    
    def dfs(self, start, nums, value_list):
        if start == len(nums):
            self.res.append(value_list)
            
            return 
            
        for i in range(len(nums)):
            nums[start] = i
            
            if self.helper(start, nums):
                self.dfs(start + 1, nums, value_list + [self.temp_value[:i] + 'Q' + self.temp_value[i + 1:]])
    
    def helper(self, end, nums):
        for i in range(end):
            if abs(nums[i] - nums[end]) == end - i or nums[i] == nums[end]:
                
                return False
 
        return True
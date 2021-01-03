class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        self.res = []
        
        self.dfs(0, candidates, target, [])
        
        return self.res
    
    def dfs(self, start, candidates, target, value_list):
        if target < 0:
            
            return
        
        if target == 0:
            self.res.append(value_list)
            
        for i in range(start, len(candidates)):
            self.dfs(i, candidates, target - candidates[i], value_list + [candidates[i]])
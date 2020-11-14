class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        self.res = []
        
        self.dfs(n, n, [])
        
        return self.res
    
    def dfs(self, start, end, value_list):
        if start > end:
            
            return
        
        if not start and not end:
            if value_list:
                self.res.append(''.join(value_list))

        if start > 0:
            self.dfs(start - 1, end, value_list + ['('])
            
        if end > 0:
            self.dfs(start, end - 1, value_list + [')'])
        
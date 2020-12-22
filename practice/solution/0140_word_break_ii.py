class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        self.value_dict = set(wordDict)
        self.res = []
        
        dp_list = self.helper(s)
        self.dfs(0, s, dp_list, [])
        
        return self.res
    
    def dfs(self, start, s, dp_list, value_list):
        if not dp_list[start + len(s)]:
            
            return
    
        if not s:
            self.res.append(' '.join(value_list))

        for i in range(1, len(s) + 1):
            if s[:i] in self.value_dict:
                self.dfs(start + i, s[i:], dp_list, value_list + [s[:i]])
    
    def helper(self, s):
        end = len(s)
        dp_list = [False] * (end + 1)
        dp_list[0] = True
        
        for i in range(end):
            for j in range(i, end + 1):
                if dp_list[i] and s[i:j] in self.value_dict:
                    dp_list[j] = True
                    
        return dp_list
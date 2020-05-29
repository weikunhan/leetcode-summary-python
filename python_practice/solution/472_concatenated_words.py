class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        self.value_dict = set(words)
        self.res = []
        
        for word in words:
            if self.dfs(word):
                self.res.append(word)
                
        return self.res
    
    def dfs(self, word):
        for i in range(1, len(word)):
            prefix_value = word[:i]
            suffix_value = word[i:]
            
            if prefix_value in self.value_dict and suffix_value in self.value_dict:
                
                return True
            
            if prefix_value in self.value_dict and self.dfs(suffix_value):
                
                return True
            
            if suffix_value in self.value_dict and self.dfs(prefix_value):
            
                return True
            
        return False
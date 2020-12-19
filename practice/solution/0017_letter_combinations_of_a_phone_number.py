class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        self.value_list = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.res = []
        
        self.res = self.dfs(digits)
        
        return self.res
        
    def dfs(self, digits):
        temp_list = []
        
        if not digits:
            
            return temp_list
        
        if len(digits) == 1:
            temp_list = list(self.value_list[int(digits[0])])
            
            return temp_list
        
        for char in self.value_list[int(digits[0])]:
            for letter in self.dfs(digits[1:]):
                temp_list.append(char + letter)
                
        return temp_list
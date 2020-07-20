class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        self.value_dict = {'2': 'abc', 
                           '3': 'def', 
                           '4': 'ghi', 
                           '5': 'jkl', 
                           '6': 'mno', 
                           '7': 'pqrs', 
                           '8': 'tuv', 
                           '9': 'wxyz'}
        self.res = []
        
        self.res = self.dfs(digits)
        
        return self.res
    
    def dfs(self, digits):
        temp_list = []
        
        if not digits:
            
            return temp_list
        
        if len(digits) == 1:
            temp_list = list(self.value_dict[digits[0]])
            
            return temp_list
        
        for char in self.value_dict[digits[0]]:
            for value in self.dfs(digits[1:]):
                temp_list.append(char + value)
                
        return temp_list
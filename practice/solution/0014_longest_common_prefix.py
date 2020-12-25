class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        value_list = sorted(strs)
        res = ''
        
        if not value_list:
            
            return res
        
        for i in range(len(value_list[0])):
            if value_list[0][i] != value_list[-1][i]:
                res = value_list[0][:i]
                
                return res
            
        res = value_list[0]
        
        return res
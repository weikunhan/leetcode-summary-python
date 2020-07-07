class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        count = 0
        value_list = sorted(strs)
        res = ''
        
        if not value_list:
            
            return res
        
        while count < len(value_list[0]) and value_list[0][count] == value_list[-1][count]:
            count += 1
            
        res = value_list[0][:count]
        
        return res
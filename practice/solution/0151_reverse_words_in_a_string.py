class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        value_list = s.split(' ')
        res = []
        
        for value in reversed(value_list):
            if value: 
                res.append(value)
            
        res = ' '.join(res)
        
        return res
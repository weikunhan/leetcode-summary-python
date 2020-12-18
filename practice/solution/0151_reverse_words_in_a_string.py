class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        value_list = s.split(' ')
        res = []
        
        for word in reversed(value_list):
            if word: 
                res.append(word)
            
        res = ' '.join(res)
        
        return res
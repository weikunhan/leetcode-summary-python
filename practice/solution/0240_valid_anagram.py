class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        res = False
        
        if sorted(s) == sorted(t):
            res = True
            
        return res
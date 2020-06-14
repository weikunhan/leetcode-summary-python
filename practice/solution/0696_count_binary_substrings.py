class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0
        right = 1
        res = 0
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                right += 1
            else:
                res += min(left, right)
                left = right
                right = 1
                
        res += min(left, right)
        
        return res
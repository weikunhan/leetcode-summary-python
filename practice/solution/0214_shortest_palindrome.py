class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
    
        temp_value = s[::-1]
        res = ''
        
        for i in range(len(s) + 1):
            if s[:len(s) - i] == temp_value[i:]:
                res = temp_value[:i] + s
                
                return res
            
        return res
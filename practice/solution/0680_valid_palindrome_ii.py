class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        value_list = []
        count = 0
        res = False
        
        while count < len(s) / 2 and s[count] == s[-(count + 1)]: 
            count += 1
            
        value_list = s[count:len(s) - count]
        
        if value_list[1:] == value_list[1:][::-1] or value_list[:-1] == value_list[:-1][::-1]:
            res = True
        
        return res
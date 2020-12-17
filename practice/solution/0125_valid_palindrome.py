class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        value_list = []
        res = False
        
        for char in s:	
            if char.isalnum(): 	
                value_list.append(char.lower())
        
        if value_list == value_list[::-1]:
            res = True
        
        return res
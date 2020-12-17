class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        value_list = [char.lower() for char in s if char.isalnum()]
        res = False
        
        if value_list == value_list[::-1]:
            res = True
        
        return res
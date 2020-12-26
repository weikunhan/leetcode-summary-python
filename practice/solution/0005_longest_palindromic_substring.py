class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        row_end = len(s)
        col_end = len(s)
        dp_list = [[False] * col_end for _ in range(row_end)]
        temp_value = 0
        res = ''
        
        for i in range(len(s)):
            dp_list[i][i] = True
            
            if i + 1 < len(s) and s[i] == s[i + 1]:
                dp_list[i][i + 1] = True
                
        for i in reversed(range(len(s) - 2)):
            for j in range(i + 2, len(s)):
                if dp_list[i + 1][j - 1] and s[j] == s[i]:
                    dp_list[i][j] = True
                    
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp_list[i][j] and j - i + 1 > temp_value:
                    temp_value = j - i + 1
                    res = s[i:i + temp_value]
                    
        return res
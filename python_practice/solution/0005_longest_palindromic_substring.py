class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        row_end = len(s)
        col_end = len(s)
        dp_list = [[False] * col_end for _ in range(row_end)]
        max_length = 0 
        res = ''
        
        for i in range(row_end):
            dp_list[i][i] = True
            
            if i < len(s) - 1 and s[i] == s[i + 1]:
                dp_list[i][i + 1] = True
                
        for i in reversed(range(row_end - 2)):
            for j in range(i + 2, col_end):
                if dp_list[i + 1][j - 1] and s[j] == s[i]:
                    dp_list[i][j] = True
                    
        for i in range(row_end):
            for j in range(col_end):
                temp_value = j - i + 1
                
                if dp_list[i][j] and temp_value > max_length:
                    max_length = temp_value
                    res = s[i:i + max_length]
                    
        return res
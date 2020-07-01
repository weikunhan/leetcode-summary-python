class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        row_end = len(p)
        col_end = len(s)
        dp_list = [[False] * (col_end + 1) for _ in range(row_end + 1)]
        dp_list[0][0] = True
        res = False
        
        for i in range(1, row_end):
            if p[i] == '*' and dp_list[i - 1][0]:
                dp_list[i + 1][0] = True
                
        for i in range(row_end):
            for j in range(col_end):
                if p[i] != '*':
                    if dp_list[i][j] and (p[i] == s[j] or p[i] == '.'):
                        dp_list[i + 1][j + 1] = True
                else:
                    if dp_list[i - 1][j + 1] or dp_list[i][j + 1]:
                        dp_list[i + 1][j + 1] = True
                        
                    if dp_list[i + 1][j] and (p[i - 1] == s[j] or p[i - 1] == '.'):
                        dp_list[i + 1][j + 1] = True
                        
                print(dp_list[i + 1][j + 1])
                            
        res = dp_list[-1][-1]
        
        return res
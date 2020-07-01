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
        dp_list[row_end][col_end] = True
        res = False
        
        for i in reversed(range(row_end)):
            if p[i] != '*':
                break

            dp_list[i][col_end] = True
        
        for i in reversed(range(row_end)):
            for j in reversed(range(col_end)):
                if p[i] != '*':
                    if  dp_list[i + 1][j + 1] and (p[i] == s[j] or p[i] == '?'):
                        dp_list[i][j] = True
                else:
                    if dp_list[i + 1][j] or dp_list[i][j + 1]:
                        dp_list[i][j] = True
                    
        res = dp_list[0][0]
        
        return res
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        row_end = len(word1)
        col_end = len(word2)
        dp_list = [[0] * (col_end + 1) for _ in range(row_end + 1)]
        res = 0
        
        for i in range(len(word1) + 1):
            dp_list[i][0] = i
            
        for i in range(len(word2) + 1):
            dp_list[0][i] = i
            
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp_list[i + 1][j + 1] = dp_list[i][j]
                else:
                    dp_list[i + 1][j + 1] = 1 + min(min(dp_list[i][j], dp_list[i + 1][j]), dp_list[i][j + 1])
                    
        res = dp_list[-1][-1]
        
        return res
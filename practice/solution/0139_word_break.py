class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        value_dict = set(wordDict)
        end = len(s)
        dp_list = [False] * (end + 1)
        dp_list[0] = True
        res = False
        
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if dp_list[i] and s[i:j] in value_dict:
                    dp_list[j] = True
                    
        res = dp_list[-1]
        
        return res
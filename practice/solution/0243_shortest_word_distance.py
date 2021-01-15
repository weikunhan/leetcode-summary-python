class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        first_value = len(words)
        second_value = len(words)
        res = sys.maxsize

        for i in range(len(words)):
            if words[i] == word1:
                first_value = i
                res = min(res, abs(first_value - second_value))
            
            if words[i] == word2:
                second_value = i
                res = min(res, abs(first_value - second_value))
                
        return res
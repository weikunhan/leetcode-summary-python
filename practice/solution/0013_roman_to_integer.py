class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        value_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        
        for i in range(len(s) - 1):
            if value_dict[s[i]] >= value_dict[s[i + 1]]:
                res += value_dict[s[i]]
            else:
                res -= value_dict[s[i]]
                
        res += value_dict[s[-1]]
        
        return res
                
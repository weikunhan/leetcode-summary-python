import collections

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        value_dict = collections.Counter()
        right = 0
        left = 0
        res = 0
        
        while right < len(s):
            temp_value = s[right]
            
            if not value_dict[temp_value]:
                k -= 1
                
            value_dict[temp_value] += 1

            while k < 0:
                value_dict[s[left]] -= 1
                
                if not value_dict[s[left]]:
                    k += 1
                    
                left += 1
                                    
            res = max(res, right - left + 1)    
            right += 1
    
        return res
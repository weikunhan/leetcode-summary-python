class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0
        right = 1
        value_dict = set()
        res = 0
        
        while right < len(s) + 1:
            temp_value = s[right - 1]
            
            while temp_value in value_dict:
                value_dict.remove(s[left])
                left += 1
            
            value_dict.add(temp_value)
            res = max(res, right - left)
            right += 1
                      
        return res
    
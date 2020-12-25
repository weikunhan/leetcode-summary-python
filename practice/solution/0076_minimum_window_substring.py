import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        right = 0
        left = 0
        start = 0
        end = 0
        value_dict = collections.Counter(t)
        max_value = len(value_dict)
        res = ''
        
        while right < len(s):
            temp_value = s[right]
            value_dict[temp_value] -= 1

            if not value_dict[temp_value]:
                max_value -= 1

            while not max_value:
                value_dict[s[left]] += 1

                if value_dict[s[left]] > 0:
                    max_value += 1
                
                if not end or end - start > right - left + 1:
                    end = right + 1
                    start = left
                    
                left += 1

            right += 1
  
        res = s[start:end]
    
        return res
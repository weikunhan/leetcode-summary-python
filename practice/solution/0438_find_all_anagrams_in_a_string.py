import collections

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        target_value_dict = collections.Counter(p)
        count_value_dict = collections.Counter(s[:len(p) - 1])
        res = []
        
        for i in range(len(p) - 1, len(s)):
            count_value_dict[s[i]] += 1
            index_value = i - len(p) + 1
            
            if count_value_dict & target_value_dict == target_value_dict:
                res.append(index_value)
                
            count_value_dict[s[index_value]] -= 1
  
        return res
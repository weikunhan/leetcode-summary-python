import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        value_dict = collections.defaultdict(list)
        res = []
        
        for char in strs:
            temp_value = ''.join(sorted(char))
            value_dict[temp_value].append(char)
                
        res = value_dict.values()
            
        return res
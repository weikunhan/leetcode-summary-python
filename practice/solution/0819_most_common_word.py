import heapq
import collections

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        value_list = re.split(r'[,\s]\s*', paragraph.lower())
        banned_value_dict = set(banned)
        data_value_dict = collections.Counter()
        res = ''
        
        for word in value_list:
            word = re.sub(r'[^a-z0-9]', '', word)
            
            if not word in banned_value_dict:
                data_value_dict[word] += 1
                
        res = heapq.nlargest(1, data_value_dict, lambda x:data_value_dict[x])[0]
        
        return res
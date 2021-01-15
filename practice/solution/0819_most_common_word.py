import collections
import heapq

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        value_list = re.split(r'[,\s]', paragraph.lower())
        data_value_dict = set(banned)
        count_value_dict = collections.Counter()
        res = ''
        
        for word in value_list:
            word_value = re.sub(r'[^a-z0-9]', '', word)
            
            if word_value and not word_value in data_value_dict:
                count_value_dict[word_value] += 1
                
        res = heapq.nlargest(1, count_value_dict, key=lambda x:count_value_dict[x])[0]
        
        return res
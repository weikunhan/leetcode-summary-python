import collections

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        data_value_dict = set(wordList)
        visit_value_dict = {beginWord: [[beginWord]]}
        res = []
        
        while visit_value_dict:
            temp_dict = collections.defaultdict(list)
            
            for word, value_list in visit_value_dict.items():
                if word == endWord:
                    res = value_list
                    
                    return res
                
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        next_value = word[:i] + char + word[i + 1:]
                        
                        if next_value in data_value_dict and not next_value in visit_value_dict:
                            for temp_list in value_list:
                                temp_dict[next_value] += [temp_list + [next_value]]
                
            for key, value in temp_dict.items():
                data_value_dict.remove(key)
                    
            visit_value_dict = temp_dict
            
        return res
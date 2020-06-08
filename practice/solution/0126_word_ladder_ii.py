import collections

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        value_dict = set(wordList)
        visit_value_dict = {beginWord:[[beginWord]]}
        res = []
        
        while visit_value_dict:
            temp_value_dict = collections.defaultdict(list)
            
            for word, nested_value_list in visit_value_dict.items():
                if word == endWord:
                    res = nested_value_list
                    
                    return res
                
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i + 1:]

                        if not new_word in visit_value_dict and new_word in value_dict:
                            for value_list in nested_value_list:
                                temp_value_dict[new_word] += [value_list + [new_word]]
                                
            value_dict -= set(temp_value_dict.keys())
            visit_value_dict = temp_value_dict
                            
        return res
import collections

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        visit_value_dict = set(wordList)
        target_value_dict = {beginWord: [[beginWord]]}
        res = []
        
        while target_value_dict:
            temp_dict = collections.defaultdict(list)
            
            for word, nested_value_list in target_value_dict.items():
                if endWord == word:
                    res = nested_value_list
                    
                    return res
                
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i + 1:]
                        
                        if not new_word in target_value_dict and new_word in visit_value_dict:
                            for value_list in nested_value_list:
                                temp_dict[new_word] += [value_list + [new_word]]
                                
            visit_value_dict -= set(temp_dict.keys())
            target_value_dict = temp_dict
            
        return res
import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        value_list = collections.deque([(beginWord, 1)])
        value_dict = set(wordList)
        res = 0
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                word, cost = value_list.popleft()
                
                if word == endWord:
                    res = cost
                    
                    return res
                
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        next_value = word[:i] + char + word[i + 1:]
                        
                        if next_value in value_dict:
                            value_list.append((next_value, cost + 1))
                            value_dict.remove(next_value)
                            
        return res
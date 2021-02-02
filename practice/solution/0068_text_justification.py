class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        value_list = []
        max_value = 0
        res = []
        
        for word in words:
            if max_value + len(word) + len(value_list) > maxWidth:
                for i in range(maxWidth - max_value):
                    if len(value_list) == 1:
                        value_list[0] += ' '
                    else:
                        value_list[i % (len(value_list) - 1)] += ' '
                        
                res.append(''.join(value_list))    
                value_list = []
                max_value = 0

            value_list.append(word)
            max_value += len(word)
            
        res.append(' '.join(value_list) + ' ' * (maxWidth - max_value - len(value_list) + 1))
        
        return res
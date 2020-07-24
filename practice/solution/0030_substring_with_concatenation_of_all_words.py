import collections

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        value_dict = collections.Counter(words)
        count = 0
        res = []
        
        if not s or not words or not words[0]:
            
            return res
        
        max_length = len(words) * len(words[0])
        word_length = len(words[0])
        
        while count < min(word_length, len(s) - max_length + 1):
            temp_dict = collections.Counter()
            left = count
            right = count

            while right + word_length < len(s) + 1:
                temp_value = s[right:right + word_length]
                right += word_length

                if not temp_value in value_dict:
                    left = right
                    temp_dict = collections.Counter()
                else:
                    temp_dict[temp_value] += 1

                    while temp_dict[temp_value] > value_dict[temp_value]:
                        temp_dict[s[left:left + word_length]] -= 1
                        left += word_length

                    if right - left == max_length:
                        res.append(left)
                         
            count += 1               
                            
        return res
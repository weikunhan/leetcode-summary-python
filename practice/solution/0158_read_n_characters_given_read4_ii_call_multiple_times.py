# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

import collections

class Solution(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.value_list = collections.deque()
        
    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        
        res = 0
        
        while res < n:
            if self.value_list:
                buf[res] = self.value_list.popleft()
                res += 1
            else:
                temp_list = [''] * 4
                temp_value = read4(temp_list)
        
                if not temp_value:
                    break
                    
                for i in range(temp_value):
                    self.value_list.append(temp_list[i])
                    
        return res

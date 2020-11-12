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

        temp_value = 0

        while temp_value < n:
            if self.value_list:
                buf[temp_value] = self.value_list.popleft()
                temp_value += 1
            else:
                temp_list = [''] * 4
                index_value = read4(temp_list)

                if not index_value:
                    break
                
                self.value_list += temp_list[:index_value]

        return temp_value

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

import collections

class Solution(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.value_list = collections.deque()
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
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
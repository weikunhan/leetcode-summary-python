class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        value_list = [''] * numRows
        count = 0
        sign = 1
        res = ''
        
        if numRows == 1 or numRows >= len(s):
            res = s
            
            return res
        
        for char in s:
            value_list[count] += char
            
            if count == 0:
                sign = 1
            
            if count == numRows - 1:
                sign = -1
                
            count += sign
            
        res = ''.join(value_list)
        
        return res
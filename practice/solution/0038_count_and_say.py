class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        res = '1'
        
        while n > 1:
            count = 1
            temp_value = ''
            
            for i in range(1, len(res)):
                if res[i] == res[i - 1]:
                    count += 1
                else:
                    temp_value += str(count) + res[i - 1]
                    count = 1
                    
            temp_value += str(count) + res[-1]
            res = temp_value
            n -= 1
            
        return res
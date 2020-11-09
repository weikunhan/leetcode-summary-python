class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        res = []
        
        for first in [1, 2, 3]:
            for second in [first + 1, first + 2, first + 3]:
                for third in [second + 1, second + 2, second + 3]:
                    if third >= len(s):
                        continue
                        
                    first_value = s[:first]
                    second_value = s[first:second]
                    third_value = s[second:third]
                    fourth_value = s[third:]
                    temp_list = [first_value, second_value, third_value, fourth_value]
                        
                    if self.helper(temp_list):
                        res.append('.'.join(temp_list))
                        
        return res
                            
    def helper(self, temp_list):
        for char in temp_list:
            if char[0] == '0' and char != '0':
                
                return False
            
            if int(char) > 255:
                
                return False
            
        return True